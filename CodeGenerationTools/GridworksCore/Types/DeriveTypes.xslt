<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl" xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xsl:output method="xml" indent="yes" />
    <xsl:param name="root" />
    <xsl:param name="codee-root" />
    <xsl:include href="../CommonXsltTemplates.xslt"/>
    <xsl:param name="exclude-collections" select="'false'" />
    <xsl:param name="relationship-suffix" select="''" />
    <xsl:variable name="airtable" select="/" />
    <xsl:variable name="squot">'</xsl:variable>
    <xsl:variable name="init-space">             </xsl:variable>
    <xsl:include href="GnfCommon.xslt"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/">
        <FileSet>
            <FileSetFiles>
                <xsl:for-each select="$airtable//ProtocolTypes/ProtocolType[(normalize-space(ProtocolName) ='gwproto')]">
                <xsl:variable name="versioned-type-id" select="VersionedType"/>
                <xsl:for-each select="$airtable//VersionedTypes/VersionedType[(VersionedTypeId = $versioned-type-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory= 'Json' or ProtocolCategory = 'GwAlgoSerial')]">
                <xsl:variable name="type-name" select="TypeName" />
                <xsl:variable name="total-attributes" select="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)])" />
                <xsl:variable name="versioned-type-name" select="VersionedTypeName"/>
                <xsl:variable name="python-class-name">
                    <xsl:if test="(normalize-space(PythonClassName) ='')">
                    <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="TypeName" />
                    </xsl:call-template>
                    </xsl:if>
                    <xsl:if test="(normalize-space(PythonClassName) != '')">
                    <xsl:value-of select="normalize-space(PythonClassName)" />
                    </xsl:if>
                </xsl:variable>
                    <xsl:variable name="overwrite-mode">

                    <xsl:if test="not (Status = 'Pending')">
                    <xsl:text>Never</xsl:text>
                    </xsl:if>
                    <xsl:if test="(Status = 'Pending')">
                    <xsl:text>Always</xsl:text>
                    </xsl:if>
                    </xsl:variable>

                    <FileSetFile>
                                <xsl:element name="RelativePath"><xsl:text>../../../src/gwproto/types/</xsl:text>
                                <xsl:value-of select="translate($type-name,'.','_')"/><xsl:text>.py</xsl:text></xsl:element>

                        <OverwriteMode><xsl:value-of select="$overwrite-mode"/></OverwriteMode>
                        <xsl:element name="FileContents">


<xsl:text>"""Type </xsl:text><xsl:value-of select="$type-name"/><xsl:text>, version </xsl:text>
<xsl:value-of select="Version"/><xsl:text>"""

import json
import logging
import os
from typing import Any, Dict</xsl:text>
	<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id) and (IsList = 'true')])>0">
<xsl:text>, List</xsl:text>
</xsl:if>
<xsl:text>, Literal</xsl:text>

<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id) and not (IsRequired = 'true')]) > 0">
<xsl:text>, Optional</xsl:text>
</xsl:if>

<xsl:if test="count(PropertyFormatsUsed)>0">
<xsl:for-each select="$airtable//PropertyFormats/PropertyFormat[(normalize-space(Name) ='AlgoAddressStringFormat')  and (count(TypesThatUse[text()=$versioned-type-id])>0)]">
<xsl:text>
import algosdk</xsl:text>
</xsl:for-each>
</xsl:if>

<xsl:text>
import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel
from pydantic import ConfigDict</xsl:text>
<xsl:text>
from pydantic import Field</xsl:text>
<xsl:if test="count($airtable//TypeAxioms/TypeAxiom[MultiPropertyAxiom=$versioned-type-id]) > 0">
<xsl:text>
from pydantic import model_validator</xsl:text>
</xsl:if>
<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id) and (IsRequired='false') or (IsEnum='true' or (IsList='true' and (IsType = 'true' or (IsPrimitive='true'  and normalize-space(PrimitiveFormat) != '') )))]) > 0">
<xsl:text>
from pydantic import field_validator</xsl:text>
</xsl:if>
<xsl:if test="count($airtable//TypeAxioms/TypeAxiom[MultiPropertyAxiom=$versioned-type-id]) > 0">
<xsl:text>
from typing_extensions import Self</xsl:text>
</xsl:if>

<xsl:if test="count(PropertyFormatsUsed)>0">
<xsl:for-each select="$airtable//PropertyFormats/PropertyFormat[(normalize-space(Name) ='MarketSlotNameLrdFormat')  and (count(TypesThatUse[text()=$versioned-type-id])>0)]">
<xsl:text>
from gw import check_is_market_slot_name_lrd_format</xsl:text>
</xsl:for-each>
</xsl:if>

<xsl:if test="MakeDataClass='true'">
<xsl:if test="not(IsComponent = 'true') and not(IsCac = 'true')">
<xsl:text>
from gwproto.data_classes.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(DataClass,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text><xsl:value-of select="DataClass"/>

</xsl:if>
</xsl:if>
<xsl:if test="IsComponent = 'true'">
<xsl:text>
from gwproto.data_classes.components.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(DataClass,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text><xsl:value-of select="DataClass"/>
</xsl:if>


<xsl:if test="IsCac = 'true'">
<xsl:text>
from gwproto.data_classes.cacs.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(DataClass,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text><xsl:value-of select="DataClass"/>
</xsl:if>

<xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">


<xsl:if test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '' or IsList = 'true')">
<xsl:text>
from gwproto.types.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(SubTypeName,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="SubTypeName" />
</xsl:call-template>
<xsl:text>
from gwproto.types.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(SubTypeName,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="SubTypeName" />
</xsl:call-template><xsl:text>Maker</xsl:text>
</xsl:if>
</xsl:for-each>

<xsl:for-each select="$airtable//GtEnums//GtEnum[normalize-space(Name) !='']">
<xsl:sort select="Name" data-type="text"/>

<xsl:variable name="base-name" select="LocalName"/>
<xsl:variable name="enum-local-name">
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="LocalName" />
</xsl:call-template>
</xsl:variable>
<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id) and (EnumLocalName[text() = $base-name])])>0">

<xsl:text>
from gwproto.enums import </xsl:text>
<xsl:value-of select="$enum-local-name"/>
</xsl:if>
</xsl:for-each>

<xsl:text>

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv('ENUM_ENCODE', "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class </xsl:text>
<xsl:value-of select="$python-class-name"/>
<xsl:text>(BaseModel):
    """
    </xsl:text>
    <!-- One line title, if it exists -->
    <xsl:if test="(normalize-space(Title) != '')">
        <xsl:value-of select="Title"/>
            <!-- With a space before the Description (if description exists)-->
            <xsl:if test="(normalize-space(Description) != '')">
                <xsl:text>.

    </xsl:text>
            </xsl:if>
    </xsl:if>

    <!-- Type Description, wrapped, if it exists -->
    <xsl:if test="(normalize-space(Description) != '')">
    <xsl:call-template name="wrap-text">
        <xsl:with-param name="text" select="normalize-space(concat(Description, ' ', UpdateDescription))"/>
        <xsl:with-param name="indent-spaces" select="4"/>
    </xsl:call-template>
    </xsl:if>


    <xsl:if test="(normalize-space(Url) != '')">
    <xsl:text>

    [More info](</xsl:text>
        <xsl:value-of select="normalize-space(Url)"/>
        <xsl:text>)</xsl:text>
    </xsl:if>
    <xsl:text>
    """

</xsl:text>
<xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
<xsl:sort select="Idx" data-type="number"/>

<xsl:variable name = "attribute-name">
    <xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"/>
        </xsl:call-template>
    <!-- If attribute is associated to a data class, add Id to the Attribute name-->
    <xsl:if test="not(normalize-space(SubTypeDataClass) = '') and not(IsList='true')">
    <xsl:text>_id</xsl:text>
    </xsl:if>
</xsl:variable>

<xsl:variable name="enum-local-name">
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="EnumLocalName" />
</xsl:call-template>
</xsl:variable>

<xsl:variable name="attribute-type">

    <!-- If Optional, start the Optional bracket-->
    <xsl:if test="not(IsRequired = 'true')">
    <xsl:text>Optional[</xsl:text>
    </xsl:if>

    <!-- If List, start the List bracket-->
    <xsl:if test="IsList = 'true'">
    <xsl:text>List[</xsl:text>
    </xsl:if>
    <xsl:choose>
    <xsl:when test="(IsPrimitive = 'true')">
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
    </xsl:when>

    <xsl:when test = "(IsEnum = 'true')">
        <xsl:value-of select="$enum-local-name"/>
    </xsl:when>

    <!-- If Attribute is a type associated with a dataclass, the reference is to its id, which is a string -->
    <xsl:when test = "not(normalize-space(SubTypeDataClass) = '') and not(IsList = 'true')">
    <xsl:text>str</xsl:text>
    </xsl:when>

    <!-- Otherwise, the reference is to the type  -->
    <xsl:when test="(IsType = 'true')">
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="SubTypeName" />
        </xsl:call-template>
    </xsl:when>
    <xsl:otherwise></xsl:otherwise>
    </xsl:choose>
            <!-- If List, end the List bracket-->
    <xsl:if test="IsList = 'true'">
    <xsl:text>]</xsl:text>
    </xsl:if>

    <!-- If Optional, end the Optional bracket-->
    <xsl:if test="not(IsRequired = 'true')">
    <xsl:text>]</xsl:text>
    </xsl:if>
</xsl:variable>

    <xsl:call-template name="insert-spaces"/>

     <!-- Name of the attribute -->
    <xsl:value-of select="$attribute-name"/><xsl:text>: </xsl:text>

    <!-- Add the attribute type (works for primitive, enum, subtype)-->
    <xsl:value-of select="$attribute-type"/>


<xsl:text> = </xsl:text>

<xsl:text>Field(
        title="</xsl:text>
        <xsl:if test="normalize-space(Title)!=''">
        <xsl:value-of select="Title"/>
        </xsl:if>
        <xsl:if test="normalize-space(Title)=''">
        <xsl:value-of select="Value"/>
        </xsl:if>
        <xsl:text>",</xsl:text>

    <!-- Add a description if either Description or URL have content -->
    <xsl:if test="(normalize-space(Description) !='') or (normalize-space(Url) != '')">

        <xsl:choose>
        <xsl:when test="(string-length(normalize-space(Description)) > 78) or ((normalize-space(Description) !='') and (normalize-space(Url) != ''))">
        <!-- For a long description, or when there is a description AND a URL  -->
        <xsl:text>
        description=(
            "</xsl:text>
        <xsl:call-template name="wrap-quoted-text">
            <xsl:with-param name="text" select="normalize-space(Description)"/>
            <xsl:with-param name="indent-spaces" select="12"/>
        </xsl:call-template>
        <xsl:text>"</xsl:text>
        <xsl:if test = "(normalize-space(Url) != '')">
        <xsl:text>
            "[More info](</xsl:text>
        <xsl:value-of select="normalize-space(Url)"/>
        <xsl:text>)"</xsl:text>
        </xsl:if>
        <xsl:text>
        ),</xsl:text>

        </xsl:when>

         <xsl:when test="normalize-space(Description) !=''">
        <!-- When there is a short non-empty description and no URL -->
        <xsl:text>
        description="</xsl:text>
        <xsl:value-of select="normalize-space(Description)"/>
        <xsl:text>",</xsl:text>
        </xsl:when>

         <xsl:when test="normalize-space(Url) !=''">
        <!-- When there is a URL only -->
        <xsl:text>
        description="</xsl:text>
        <xsl:text>[More info](</xsl:text>
        <xsl:value-of select="normalize-space(Url)"/>
        <xsl:text>)",</xsl:text>
        </xsl:when>

        <xsl:otherwise>
        <!-- When there is no URL and no Description, do not include description in the Field -->
        </xsl:otherwise>

        </xsl:choose>

    </xsl:if>

<!-- SETTING DEFAULT VALUE FOR ATTRIBUTE IN CLASS DECLARATION -->
    <xsl:choose>

    <!-- If the attribute is not required, choose the default to always be none-->
    <xsl:when test= "not (IsRequired = 'true')">
    <xsl:text>
        default=None,</xsl:text>
    </xsl:when>

    <!-- Else if a default value is specified, use that -->
    <xsl:when test="(normalize-space(DefaultValue) !='')">
        <xsl:text>
        default=</xsl:text>
         <xsl:if test="IsEnum='true'">
             <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="EnumLocalName" />
            </xsl:call-template><xsl:text>.</xsl:text>
         </xsl:if>
        <xsl:value-of select="DefaultValue"/>
        <xsl:text>,</xsl:text>
    </xsl:when>
    <xsl:otherwise>
    </xsl:otherwise>
    </xsl:choose>

    <xsl:text>
    )
</xsl:text>
<!-- End of declaring the attributes of the class-->
</xsl:for-each>


<xsl:text>    type_name: Literal["</xsl:text><xsl:value-of select="TypeName"/><xsl:text>"] = "</xsl:text><xsl:value-of select="TypeName"/><xsl:text>"
    version: Literal["</xsl:text>
<xsl:value-of select="Version"/><xsl:text>"] = "</xsl:text><xsl:value-of select="Version"/><xsl:text>"</xsl:text>

<xsl:if test="ExtraAllowed='true'"><xsl:text>

    model_config = ConfigDict(
        extra="allow", alias_generator=snake_to_pascal, populate_by_name=True
    )</xsl:text>
</xsl:if>
<xsl:if test="not(ExtraAllowed='true')"><xsl:text>

    model_config = ConfigDict(
        alias_generator=snake_to_pascal, populate_by_name=True
    )</xsl:text>
</xsl:if>

<!-- CONSTRUCTING VALIDATORS CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS -->
<!-- CONSTRUCTING VALIDATORS CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS -->
<!-- CONSTRUCTING VALIDATORS CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS -->
<!-- CONSTRUCTING VALIDATORS CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS  CONSTRUCTING VALIDATORS -->

    <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
    <xsl:sort select="Idx" data-type="number"/>
    <xsl:variable name="type-attribute-id" select="TypeAttributeId" />

    <xsl:variable name="enum-local-name">
        <xsl:if test = "(IsEnum = 'true')">
            <xsl:call-template name="nt-case">
                            <xsl:with-param name="type-name-text" select="EnumLocalName" />
            </xsl:call-template>
        </xsl:if>
    </xsl:variable>

    <xsl:variable name="attribute-type">

        <!-- If Optional, start the Optional bracket-->
        <xsl:if test="not(IsRequired = 'true')">
        <xsl:text>Optional[</xsl:text>
        </xsl:if>

        <!-- If List, start the List bracket-->
        <xsl:if test="IsList = 'true'">
        <xsl:text>List[</xsl:text>
        </xsl:if>
        <xsl:choose>
        <xsl:when test="(IsPrimitive = 'true')">
        <xsl:call-template name="python-type">
            <xsl:with-param name="gw-type" select="PrimitiveType"/>
        </xsl:call-template>
        </xsl:when>

        <xsl:when test = "(IsEnum = 'true')">
            <xsl:value-of select="$enum-local-name"/>
        </xsl:when>

        <!-- If Attribute is a type associated with a dataclass, the reference is to its id, which is a string -->
        <xsl:when test = "not(normalize-space(SubTypeDataClass) = '')">
        <xsl:text>str</xsl:text>
        </xsl:when>

        <!-- Otherwise, the reference is to the type  -->
        <xsl:when test="(IsType = 'true')">
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="SubTypeName" />
            </xsl:call-template>
        </xsl:when>
        <xsl:otherwise></xsl:otherwise>
        </xsl:choose>
                <!-- If List, end the List bracket-->
        <xsl:if test="IsList = 'true'">
        <xsl:text>]</xsl:text>
        </xsl:if>

        <!-- If Optional, end the Optional bracket-->
        <xsl:if test="not(IsRequired = 'true')">
        <xsl:text>]</xsl:text>
        </xsl:if>
    </xsl:variable>

    <xsl:variable name = "attribute-name">
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"/>
            </xsl:call-template>
        <!-- If attribute is associated to a data class, add Id to the Attribute name-->
        <xsl:if test="not(normalize-space(SubTypeDataClass) = '') and not(IsList='true')">
        <xsl:text>_id</xsl:text>
        </xsl:if>
    </xsl:variable>

    <xsl:if test="(IsList='true' and PrimitiveType != '' and normalize-space(Format) != '') or (normalize-space(PrimitiveFormat) != '') or (Axiom != '') or (normalize-space(SubTypeDataClass) != '' and not(IsList='true'))">

    <xsl:text>

    @field_validator("</xsl:text><xsl:value-of select="$attribute-name"/><xsl:text>"</xsl:text>

    <xsl:if test="PreValidateFormat='true'">
    <xsl:text>, mode='before'</xsl:text>
    </xsl:if>
    <xsl:text>)
    @classmethod
    def </xsl:text>

    <!-- add an underscore if there are no axioms getting checked, in which case its just property formats and/or enums -->
    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]) = 0">
    <xsl:text>_</xsl:text>
    </xsl:if>

    <xsl:text>check_</xsl:text><xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="$attribute-name"  />
        </xsl:call-template><xsl:text>(cls, v: </xsl:text>
        <xsl:value-of select="$attribute-type"/>
        <xsl:text>) -> </xsl:text>
        <xsl:value-of select="$attribute-type"/>
        <xsl:text>:</xsl:text>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]) > 1">
        <xsl:text>
        """
        Axioms </xsl:text>
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>
        <xsl:value-of select="AxiomNumber"/>
                <xsl:if test="position() != count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)])">
                <xsl:text>, </xsl:text>
                </xsl:if>
        </xsl:for-each>
        <xsl:text>:</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]) = 1">
        <xsl:text>
        """</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]) > 0">
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]) =1">
        <xsl:text>
        Axiom </xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]) >1">
        <xsl:text>

        Axiom </xsl:text>
        </xsl:if>

        <xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/>

        <xsl:if test="normalize-space(Description)!=''">
        <xsl:text>.
        </xsl:text>
         <xsl:call-template name="wrap-text">
        <xsl:with-param name="text" select="normalize-space(Description)"/>
        </xsl:call-template>
        </xsl:if>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text><xsl:value-of select="Url"/>
        <xsl:text>)</xsl:text>

        </xsl:if>

        </xsl:for-each>
        <xsl:text>
        """</xsl:text>
        </xsl:if>



        <xsl:if test="not(IsRequired = 'true')">
                <xsl:text>
        if v is None:
            return v</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$type-attribute-id)]) > 0">
        <xsl:text>
        ...
        # TODO: Implement Axiom(s)</xsl:text>
        </xsl:if>

        <xsl:choose>

        <!-- Format needs validating; not a list-->
        <xsl:when test="normalize-space(PrimitiveFormat) !='' and not(IsList='true')">
        <xsl:text>
        try:
            check_is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
                </xsl:call-template>
        <xsl:text>(v)
        except ValueError as e:</xsl:text>
        <xsl:choose>
            <xsl:when test="string-length(PrimitiveFormat) + string-length(Value)> 24">
            <xsl:text>
            raise ValueError(
                f"</xsl:text><xsl:value-of select="Value"/><xsl:text> failed </xsl:text>
            <xsl:value-of select="PrimitiveFormat"/>
            <xsl:text> format validation: {e}",
            ) from e</xsl:text>
            </xsl:when>
            <xsl:otherwise>
            <xsl:text>
            raise ValueError(f"</xsl:text><xsl:value-of select="Value"/><xsl:text> failed </xsl:text>
            <xsl:value-of select="PrimitiveFormat"/>
            <xsl:text> format validation: {e}") from e</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text>
        return v</xsl:text>
        </xsl:when>

        <!-- Format needs validating; is a list-->
        <xsl:when test="normalize-space(PrimitiveFormat) !='' and (IsList='true')">
        <xsl:text>
        for elt in v:
            try:
                check_is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
            </xsl:call-template>
        <xsl:text>(elt)
            except ValueError as e:
                raise ValueError(
                    f"</xsl:text><xsl:value-of select="Value"/><xsl:text> element {elt} failed </xsl:text>
                <xsl:value-of select="PrimitiveFormat" />
                <xsl:text> format validation: {e}",
                ) from e
        return v</xsl:text>
        </xsl:when>

         <!-- SubType w Data Class; not a list-->
        <xsl:when test = "not(normalize-space(SubTypeDataClass) = '') and not(IsList='true')">
        <xsl:text>
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"</xsl:text>
                <xsl:value-of select="Value"/><xsl:text>Id failed UuidCanonicalTextual format validation: {e}",
            ) from e
        return v</xsl:text>
        </xsl:when>

         <!-- SubType w Data Class; is a list-->
        <xsl:when test="not(normalize-space(SubTypeDataClass) = '') and IsList='true'">
        <xsl:text>
        for elt in v:
            try:
                check_is_uuid_canonical_textual(elt)
            except ValueError as e:
                raise ValueError(
                    f"</xsl:text><xsl:value-of select="Value"/><xsl:text> element {elt} failed </xsl:text>
                <xsl:value-of select="PrimitiveFormat" />
                <xsl:text> format validation: {e}",
                ) from e
        return v</xsl:text>
        </xsl:when>

        <xsl:otherwise>
        </xsl:otherwise>
        </xsl:choose>
    </xsl:if>

        </xsl:for-each>


    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[MultiPropertyAxiom=$versioned-type-id]) > 0">
    <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[MultiPropertyAxiom=$versioned-type-id]">
    <xsl:sort select="AxiomNumber" data-type="number"/>
    <xsl:text>

    @model_validator</xsl:text>
    <xsl:if test="CheckFirst='true'">
     <xsl:text>(mode='before')</xsl:text>
    </xsl:if>
    <xsl:if test="not(CheckFirst='true')">
     <xsl:text>(mode='after')</xsl:text>
    </xsl:if>
    <xsl:text>
    def check_axiom_</xsl:text><xsl:value-of select="AxiomNumber"/><xsl:text>(self) -> Self:
        """
        Axiom </xsl:text><xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/>
        <xsl:text>.
        </xsl:text><xsl:value-of select="Description"/>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text>
        <xsl:value-of select="normalize-space(Url)"/>
        <xsl:text>)</xsl:text>
        </xsl:if>

        <xsl:text>
        """
        # TODO: Implement check for axiom </xsl:text><xsl:value-of select="AxiomNumber"/><xsl:text>"
        return self</xsl:text>

    </xsl:for-each>
    </xsl:if>


    <!-- DONE WITH VALIDATORS  -->
    <!-- DONE WITH VALIDATORS  -->



    <!-- AS_DICT ######################################################################-->
    <!-- AS_DICT ######################################################################-->
    <!-- AS_DICT ######################################################################-->
    <!-- AS_DICT ######################################################################-->
    <xsl:text>

    def as_dict(self) -> Dict[str, Any]:
        """
        Main step in serializing the object. Encodes enums as their 8-digit random hex symbol if
        settings.encode_enums = 1.
        """
        if ENCODE_ENUMS:
            return self.enum_encoded_dict()
        else:
            return self.plain_enum_dict()

    def plain_enum_dict(self) -> Dict[str, Any]:
        """
        Returns enums as their values.
        """
        d = {
            snake_to_pascal(key): value
            for key, value in self.model_dump().items()
            if value is not None
        }</xsl:text>

        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>
    <xsl:choose>

    <!-- (Required) CASES FOR as_dict -->
    <xsl:when test="IsRequired = 'true'">
    <xsl:choose>

        <!-- (required) as_dict: Single Enums -->
        <xsl:when test="(IsEnum = 'true') and not (IsList = 'true')">
    <xsl:text>
        d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"] = d["</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>"].value</xsl:text>
        </xsl:when>

         <!-- (required) as_dict: List of Enums -->
        <xsl:when test="(IsEnum = 'true')  and (IsList = 'true')">
        <xsl:text>
        del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template> <xsl:text> = []
        for elt in self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>:
            </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>.append(elt.value)
        d["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>

        <!--(required) as_dict: Single Type, no associated data class (since those just show up as id pointers) -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and not (IsList = 'true')">
        <xsl:text>
        d["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"] = self.</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template>
            <xsl:text>.as_dict()</xsl:text>
        </xsl:when>


        <!-- (required) as_dict: List of Types -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '' or IsList='true') and (IsList = 'true')">
        <xsl:text>
        # Recursively calling as_dict()
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
        for elt in self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>:
            </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>.append(elt.as_dict())
        d["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>
        <xsl:otherwise></xsl:otherwise>
    </xsl:choose>
    </xsl:when>

    <!-- Optional as_dict -->
    <xsl:otherwise>
        <xsl:choose>

        <!-- (optional) as_dict: Single Enums -->
        <xsl:when test="(IsEnum = 'true') and not (IsList = 'true')">
    <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"] = d["</xsl:text>
            <xsl:value-of select="Value"/><xsl:text>"].value</xsl:text>
        </xsl:when>

         <!-- (optional) as_dict: List of Enums -->
        <xsl:when test="(IsEnum = 'true')  and (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
            </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template> <xsl:text> = []
            for elt in self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>:
                </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>.append(elt.value)
            d["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>

        <!--(optional) as_dict: Single Type, no associated data class (since those just show up as id pointers) -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and not (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
            d["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"] = self.</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>.as_dict()</xsl:text>
        </xsl:when>

        <!-- (optional) as_dict: List of Types -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
            for elt in self.</xsl:text>
       <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>:
                </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>.append(elt.as_dict())
            d["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>
         <!-- End of loop inside optional -->
        <xsl:otherwise></xsl:otherwise>
        </xsl:choose>


    </xsl:otherwise>
    </xsl:choose>

    </xsl:for-each>
    <xsl:text>
        return d

    def enum_encoded_dict(self) -> Dict[str, Any]:
        """
        Encodes enums as their 8-digit random hex symbol
        """
        d = {
            snake_to_pascal(key): value
            for key, value in self.model_dump().items()
            if value is not None
        }</xsl:text>

        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>

        <xsl:variable name="enum-local-name">
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="EnumLocalName" />
            </xsl:call-template>
        </xsl:variable>
    <xsl:choose>

    <!-- (Required) CASES FOR as_dict -->
    <xsl:when test="IsRequired = 'true'">
    <xsl:choose>

        <!-- (required) as_dict: Single Enums -->
        <xsl:when test="(IsEnum = 'true') and not (IsList = 'true')">
    <xsl:text>
        del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
        d["</xsl:text>
        <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template>
        <xsl:text>GtEnumSymbol"] = </xsl:text><xsl:value-of select="$enum-local-name"/>
        <xsl:text>.value_to_symbol(self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"/>
        </xsl:call-template>
        <xsl:text>)</xsl:text>
        </xsl:when>

         <!-- (required) as_dict: List of Enums -->
        <xsl:when test="(IsEnum = 'true')  and (IsList = 'true')">
        <xsl:text>
        del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template> <xsl:text> = []
        for elt in self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>:
            </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>.append(</xsl:text>
        <xsl:value-of select="$enum-local-name"/><xsl:text>.value_to_symbol(elt.value))
        d["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>

        <!--(required) as_dict: Single Type, no associated data class (since those just show up as id pointers) -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and not (IsList = 'true')">
        <xsl:text>
        d["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"] = self.</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template>
            <xsl:text>.as_dict()</xsl:text>
        </xsl:when>


        <!-- (required) as_dict: List of Types -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '' or IsList='true') and (IsList = 'true')">
        <xsl:text>
        # Recursively calling as_dict()
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
        for elt in self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>:
            </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>.append(elt.as_dict())
        d["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>
        <xsl:otherwise></xsl:otherwise>
    </xsl:choose>
    </xsl:when>

    <!-- Optional as_dict -->
    <xsl:otherwise>
        <xsl:choose>

        <!-- (optional) as_dict: Single Enums -->
        <xsl:when test="(IsEnum = 'true') and not (IsList = 'true')">
    <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
            d["</xsl:text>
        <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template>
        <xsl:text>GtEnumSymbol"] = </xsl:text><xsl:value-of select="$enum-local-name"/>
        <xsl:text>.value_to_symbol(self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>)</xsl:text>
        </xsl:when>

         <!-- (optional) as_dict: List of Enums -->
        <xsl:when test="(IsEnum = 'true')  and (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
            </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template> <xsl:text> = []
            for elt in self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>:
                </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>.append(</xsl:text>
        <xsl:value-of select="$enum-local-name"/><xsl:text>.value_to_symbol(elt.value))
            d["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>

        <!--(optional) as_dict: Single Type, no associated data class (since those just show up as id pointers) -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and not (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
            d["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"] = self.</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>.as_dict()</xsl:text>
        </xsl:when>

        <!-- (optional) as_dict: List of Types -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>" in d.keys():
            </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
            for elt in self.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>:
                </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>.append(elt.as_dict())
            d["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>
         <!-- End of loop inside optional -->
        <xsl:otherwise></xsl:otherwise>
        </xsl:choose>


    </xsl:otherwise>
    </xsl:choose>

    </xsl:for-each>
    <xsl:text>
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the </xsl:text>
        <xsl:value-of select="VersionedTypeName"/>
        <xsl:text> representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class </xsl:text>
    <xsl:value-of select="$python-class-name"/>
    <xsl:text>Maker:
    type_name = "</xsl:text><xsl:value-of select="TypeName"/><xsl:text>"
    version = "</xsl:text><xsl:value-of select="Version"/><xsl:text>"

    @classmethod
    def tuple_to_type(cls, tuple: </xsl:text><xsl:value-of select="$python-class-name"/>
    <xsl:text>) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> </xsl:text><xsl:value-of select="$python-class-name"/>
<xsl:text>:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a </xsl:text>
        <xsl:value-of select="VersionedTypeName"/>  <xsl:text> type

        Returns:
            </xsl:text><xsl:value-of select="$python-class-name"/><xsl:text> instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n &lt;{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> </xsl:text><xsl:value-of select="$python-class-name"/>
    <xsl:text>:
        """
        Translates a dict representation of a </xsl:text><xsl:value-of select="VersionedTypeName"/>
        <xsl:text> message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)</xsl:text>

<xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
<xsl:sort select="Idx" data-type="number"/>
<xsl:variable name="enum-local-name">
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="EnumLocalName" />
    </xsl:call-template>
</xsl:variable>

    <xsl:choose>

    <!-- Check for enum or type -->
    <xsl:when test="(IsEnum = 'true') or (IsType = 'true' and (normalize-space(SubTypeDataClass) = '' or IsList='true'))">
    <!-- OUTER LOOP dict_to_tuple -->
    <xsl:choose>

     <!-- OUTER LOOP dict_to_tuple: attribute is required-->
    <xsl:when test= "IsRequired='true'">
        <!-- INNER LOOP dict_to_tuple -->
        <xsl:choose>
            <!-- (Is required) INNER LOOP dict_to_tuple: Single Enum -->
        <xsl:when test="(IsEnum = 'true') and not (IsList = 'true')">
        <xsl:text>
        if "</xsl:text>
            <xsl:value-of select="Value"/>
         <xsl:text>GtEnumSymbol" in d2.keys():
            value = </xsl:text>
        <xsl:value-of select="$enum-local-name"/>
        <xsl:text>.symbol_to_value(d2["</xsl:text>
        <xsl:value-of select="Value" />
        <xsl:text>GtEnumSymbol"])
            d2["</xsl:text> <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template><xsl:text>"] = </xsl:text>
        <xsl:value-of select="$enum-local-name"/>
        <xsl:text>(value)
            del d2["</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>GtEnumSymbol"]
        elif "</xsl:text>
            <xsl:value-of select="Value" />
         <xsl:text>" in d2.keys():
            if d2["</xsl:text>
                <xsl:value-of select="Value"/><xsl:text>"] not in </xsl:text>
            <xsl:value-of select="$enum-local-name"/><xsl:text>.values():
                d2["</xsl:text>
                <xsl:value-of select="Value"/><xsl:text>"] = </xsl:text>
                <xsl:value-of select="$enum-local-name"/><xsl:text>.default()
            else:
                d2["</xsl:text>
                <xsl:value-of select="Value"/><xsl:text>"] = </xsl:text>
            <xsl:value-of select="$enum-local-name"/>
            <xsl:text>(d2["</xsl:text>
                <xsl:value-of select="Value"/><xsl:text>"])
        else:
            raise GwTypeError(
                f"both </xsl:text>
            <xsl:value-of select="Value" />
            <xsl:text>GtEnumSymbol and </xsl:text>
            <xsl:value-of select="Value" />
            <xsl:text> missing from dict &lt;{d2}>",
            )</xsl:text>

        </xsl:when>

        <!-- (Is required) INNER LOOP dict_to_tuple:  Enum List -->
        <xsl:when test="(IsEnum = 'true') and (IsList = 'true')">
        <xsl:text>
        if "</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>" not in d2.keys():
            raise GwTypeError(f"dict &lt;{d2}> missing </xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>")
        if not isinstance(d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"], List):
            raise GwTypeError("</xsl:text><xsl:value-of select="Value"/><xsl:text> must be a List!")
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
        for elt in d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"]:
            if elt in </xsl:text>
            <xsl:value-of select="$enum-local-name"/><xsl:text>.symbols():
                value = </xsl:text>
            <xsl:value-of select="$enum-local-name"/><xsl:text>.symbol_to_value(elt)
            elif elt in </xsl:text>
            <xsl:value-of select="$enum-local-name"/><xsl:text>.values():
                value = elt
            else:
                value = </xsl:text>
            <xsl:value-of select="$enum-local-name"/><xsl:text>.default()
            </xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template>
            <xsl:text>.append(</xsl:text>
            <xsl:value-of select="$enum-local-name"/><xsl:text>(value))
        d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>

         <!-- (Is required) INNER LOOP dict_to_tuple: Single type not Dataclass -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and not (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" not in d2.keys():
            raise GwTypeError(f"dict missing </xsl:text><xsl:value-of select="Value"/><xsl:text>: &lt;{d2}>")
        if not isinstance(d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"], dict):
            raise GwTypeError(
                f"</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text> &lt;{d2['</xsl:text><xsl:value-of select="Value"/>
            <xsl:text>']}> must be a </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="SubTypeName" />
            </xsl:call-template>
            <xsl:text>!"
            )
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="SubTypeName" />
        </xsl:call-template>
        <xsl:text>Maker.dict_to_tuple(
            d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"]
        )
        d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>

        <!-- (Is required) INNER LOOP dict_to_tuple: List of types (can be data class) -->
        <xsl:when test="(IsType = 'true') and (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" not in d2.keys():
            raise GwTypeError(f"dict missing </xsl:text><xsl:value-of select="Value"/><xsl:text>: &lt;{d2}>")
        if not isinstance(d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"], List):
            raise GwTypeError(f"</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text> &lt;{d2['</xsl:text><xsl:value-of select="Value"/>
            <xsl:text>']}> must be a List!")
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
        for elt in d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"]:
            if not isinstance(elt, dict):
                raise GwTypeError(
                    f"</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text> &lt;{d2['</xsl:text><xsl:value-of select="Value"/>
            <xsl:text>']}> must be a List of </xsl:text>
            <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="SubTypeName" />
            </xsl:call-template>
            <xsl:text> types"
                )
            t = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="SubTypeName" />
        </xsl:call-template>
        <xsl:text>Maker.dict_to_tuple(elt)
            </xsl:text><xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>.append(t)
        d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:when>

        <!-- Completing REQUIRED inner loop choose-->
        <xsl:otherwise></xsl:otherwise>
        </xsl:choose>
    </xsl:when>

     <!-- OUTER LOOP dict_to_tuple: attribute is optional-->
    <xsl:otherwise>


        <xsl:choose>

        <!-- (Is required) INNER LOOP dict_to_tuple: Single Enum -->
        <xsl:when test="(IsEnum = 'true') and not (IsList = 'true')">
            <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" in d2.keys():
            if d2["</xsl:text><xsl:value-of select="Value"/>
            <xsl:text>"] not in </xsl:text>
            <xsl:value-of select="$enum-local-name"/><xsl:text>.values():
                d2["</xsl:text><xsl:value-of select="Value"/>
                <xsl:text>"] = </xsl:text>
                <xsl:value-of select="$enum-local-name"/><xsl:text>.default()
            else:
                d2["</xsl:text><xsl:value-of select="Value"/>
                <xsl:text>"] = </xsl:text>
                <xsl:value-of select="$enum-local-name"/><xsl:text>(d2["</xsl:text>
                <xsl:value-of select="Value"/><xsl:text>"])
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>GtEnumSymbol" in d2.keys():
            value = </xsl:text>
            <xsl:value-of select="$enum-local-name"/>
            <xsl:text>.symbol_to_value(d2["</xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="Value" />
            </xsl:call-template><xsl:text>GtEnumSymbol"])
            d2["</xsl:text> <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="Value" />
            </xsl:call-template><xsl:text>"] = </xsl:text>
            <xsl:value-of select="$enum-local-name"/>
            <xsl:text>(value)
            del d2["</xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="Value" />
            </xsl:call-template><xsl:text>GtEnumSymbol"]</xsl:text>
        </xsl:when>


        <!-- (Is optional) INNER LOOP dict_to_tuple: Single type not Dataclass -->
        <xsl:when test="(IsType = 'true') and (normalize-space(SubTypeDataClass) = '') and not (IsList = 'true')">
        <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" in d2.keys():
            if not isinstance(d2["</xsl:text><xsl:value-of select="Value"/>
            <xsl:text>"], dict):
                raise GwTypeError(f"d['</xsl:text>
                <xsl:value-of select="Value"/>
                <xsl:text>'] &lt;{d2['</xsl:text><xsl:value-of select="Value"/>
                <xsl:text>']}> must be a </xsl:text>
                <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="SubTypeName" />
                </xsl:call-template>
                <xsl:text>!")
            </xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template>
            <xsl:text> = </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="SubTypeName" />
            </xsl:call-template>
            <xsl:text>_Maker.dict_to_tuple(d2["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"])
            d2["</xsl:text><xsl:value-of select="Value"/>
            <xsl:text>"] = </xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template>
            </xsl:when>

         <!-- Completing OPTIONAL inner loop choose-->
        <xsl:otherwise></xsl:otherwise>
        </xsl:choose>

    </xsl:otherwise>
    </xsl:choose>

    <!-- Finishing clause testing for enum or type -->
    </xsl:when>
    <xsl:otherwise>
    <xsl:if test="IsRequired='true'">
    <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/>

        <xsl:if test="not(normalize-space(SubTypeDataClass) = '') and not(IsList='true')">
        <xsl:text>Id</xsl:text>
        </xsl:if>


        <xsl:text>" not in d2.keys():
            raise GwTypeError(f"dict missing </xsl:text><xsl:value-of select="Value"/><xsl:text>: &lt;{d2}>")</xsl:text>

    </xsl:if>

    </xsl:otherwise>
    </xsl:choose>
<!-- finishing for-each for dict_to_tuple attributes-->
</xsl:for-each>


<xsl:text>
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict &lt;{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict &lt;{d2}>")
        if d2["Version"] != "</xsl:text><xsl:value-of select="Version"/><xsl:text>":
            LOGGER.debug(
                f"Attempting to interpret </xsl:text>
            <xsl:value-of select="TypeName"/>
            <xsl:text> version {d2['Version']} as version </xsl:text>
            <xsl:value-of select="Version"/> <xsl:text>"
            )
            d2["Version"] = "</xsl:text><xsl:value-of select="Version"/><xsl:text>"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return </xsl:text><xsl:value-of select="$python-class-name"/><xsl:text>(**d3)</xsl:text>
    <xsl:if test="(MakeDataClass='true')">
    <xsl:text>

    @classmethod
    def tuple_to_dc(cls, t: </xsl:text><xsl:value-of select="$python-class-name"/>
    <xsl:text>) -> </xsl:text><xsl:value-of select="DataClass"/><xsl:text>:
        if t.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="DataClassIdField"/>
        </xsl:call-template>
        <xsl:text> in </xsl:text>
        <xsl:value-of select="DataClass"/><xsl:text>.by_id.keys():
            dc = </xsl:text><xsl:value-of select="DataClass"/><xsl:text>.by_id[t.</xsl:text>
             <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="DataClassIdField"/>
        </xsl:call-template><xsl:text>]
        else:
            dc = </xsl:text><xsl:value-of select="DataClass"/><xsl:text>(
                </xsl:text>
        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>
        <xsl:choose>

        <!-- Single type associated with a single dataclass -->
        <xsl:when test="not(normalize-space(SubTypeDataClass) = '') and not(IsList = 'true')">
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template><xsl:text>_id=t.</xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"/>
                </xsl:call-template>
    <xsl:text>_id</xsl:text>
        </xsl:when>
        <!-- For all other classes -->
        <xsl:otherwise>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template><xsl:text>=t.</xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"/>
                </xsl:call-template>

        </xsl:otherwise>

        </xsl:choose>
                <xsl:variable name="current-attribute" select="position()" />
                <xsl:choose>
                <xsl:when test="$current-attribute=$total-attributes">
                <xsl:text>,</xsl:text>
                </xsl:when>
                <xsl:otherwise>
                <xsl:text>,
                </xsl:text>
                </xsl:otherwise>
                </xsl:choose>


    </xsl:for-each>
            <xsl:text>
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: </xsl:text><xsl:value-of select="DataClass"/><xsl:text>) -> </xsl:text><xsl:value-of select="$python-class-name"/><xsl:text>:
        return </xsl:text><xsl:value-of select="$python-class-name"/><xsl:text>(
            </xsl:text>
        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>
        <xsl:choose>
        <!-- Single type associated with a single dataclass -->
        <xsl:when test="not(normalize-space(SubTypeDataClass) = '') and not(IsList = 'true')">
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"/>
            </xsl:call-template>
        <xsl:text>_id=dc.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>_id,
            </xsl:text>
        </xsl:when>

         <!-- For all other classes -->
        <xsl:otherwise>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"/>
            </xsl:call-template>
        <xsl:text>=dc.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>


            <xsl:variable name="current-attribute" select="position()" />
            <xsl:choose>
            <xsl:when test="$current-attribute=$total-attributes">
            <xsl:text>,</xsl:text>
            </xsl:when>
            <xsl:otherwise>
            <xsl:text>,
            </xsl:text>
            </xsl:otherwise>
            </xsl:choose>


        </xsl:otherwise>
        </xsl:choose>


        </xsl:for-each>
        <xsl:text>
        )

    @classmethod
    def type_to_dc(cls, t: str) -> </xsl:text><xsl:value-of select="DataClass"/><xsl:text>:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: </xsl:text><xsl:value-of select="DataClass"/><xsl:text>) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> </xsl:text><xsl:value-of select="DataClass"/><xsl:text>:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))</xsl:text>
</xsl:if>


<xsl:for-each select="$airtable//GtEnums/GtEnum[(normalize-space(Name) !='')  and (count(TypesThatUse[text()=$versioned-type-id])>0)]">
<xsl:variable name="local-name" select="LocalName"/>
<xsl:variable name="enum-local-name">
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="LocalName" />
    </xsl:call-template>
</xsl:variable>
<xsl:variable name="enum-id" select="GtEnumId"/>
<xsl:variable name="enum-version" select="Version"/>




</xsl:for-each>

<xsl:if test="count(PropertyFormatsUsed)>0">
<xsl:for-each select="$airtable//PropertyFormats/PropertyFormat[(normalize-space(Name) !='')  and (count(TypesThatUse[text()=$versioned-type-id])>0)]">
<xsl:sort select="Name" data-type="text"/>
<xsl:choose>
    <xsl:when test="Name='Ads1115I2cAddress'">
    <xsl:text>


def check_is_ads1115_i2c_address(v: str) -> None:
    """
    Ads1115I2cAddress: ToLower(v) in  ['0x48', '0x49', '0x4a', '0x4b'].

    One of the 4 allowable I2C addresses for Texas Instrument Ads1115 chips.

    Raises:
        ValueError: if not Ads1115I2cAddress format
    """
    if v.lower() not in  ['0x48', '0x49', '0x4a', '0x4b']:
        raise ValueError(f"Not Ads1115I2cAddress: &lt;{v}>")</xsl:text>

    </xsl:when>

    <xsl:when test="Name='AlgoAddressStringFormat'">
    <xsl:text>


def check_is_algo_address_string_format(v: str) -> None:
    """
    AlgoAddressStringFormat format: The public key of a private/public Ed25519
    key pair, transformed into an  Algorand address, by adding a 4-byte checksum
    to the end of the public key and then encoding in base32.

    Raises:
        ValueError: if not AlgoAddressStringFormat format
    """

    at = algosdk.abi.AddressType()
    try:
        at.decode(at.encode(v))
    except Exception as e:
        raise ValueError(f"Not AlgoAddressStringFormat: {e}") from e</xsl:text>
    </xsl:when>


    <xsl:when test="Name='AlgoMsgPackEncoded'">
    <xsl:text>


def check_is_algo_msg_pack_encoded(v: str) -> None:
    """
    AlgoMSgPackEncoded format: the format of a transaction sent to
    the Algorand blockchain. Error is not thrown with
    algosdk.encoding.future_msg_decode(candidate)

    Raises:
        ValueError: if not AlgoMSgPackEncoded  format
    """

    try:
        algosdk.encoding.future_msgpack_decode(v)
    except Exception as e:
        raise ValueError(f"Not AlgoMsgPackEncoded format: {e}") from e</xsl:text>
    </xsl:when>

    <xsl:when test="Name='Bit'">
    <xsl:text>


def check_is_bit(v: int) -> None:
    """
    Checks Bit format

    Bit format: The value must be the integer 0 or the integer 1.

    Will not attempt to first interpret as an integer. For example,
    1.3 will not be interpreted as 1 but will raise an error.

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v is not 0 or 1
    """
    if not v in [0,1]:
        raise ValueError(f"&lt;{v}> must be 0 or 1")</xsl:text>

    </xsl:when>

    <xsl:when test="Name='HexChar'">
    <xsl:text>


def check_is_hex_char(v: str) -> None:
    """Checks HexChar format

    HexChar format: single-char string in '0123456789abcdefABCDEF'

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not HexChar format
    """
    if not isinstance(v, str):
        raise ValueError(f"&lt;{v}> must be a hex char, but not even a string")
    if len(v) > 1:
        raise ValueError(f"&lt;{v}> must be a hex char, but not of len 1")
    if v not in "0123456789abcdefABCDEF":
        raise ValueError(f"&lt;{v}> must be one of '0123456789abcdefABCDEF'")</xsl:text>
    </xsl:when>


    <xsl:when test="Name='IsoFormat'">
    <xsl:text>


def check_is_iso_format(v: str) -> None:
    """
    Example: '2024-01-10T15:30:45.123456-05:00'  The string does not
    need to include microseconds.
    """
    import datetime

    try:
        datetime.datetime.fromisoformat(v.replace("Z", "+00:00"))
    except Exception as e:
        raise ValueError(f"&lt;{v}> is not IsoFormat") from e</xsl:text>
    </xsl:when>


    <xsl:when test="Name='LeftRightDot'">
    <xsl:text>


def check_is_left_right_dot(v: str) -> None:
    """Checks LeftRightDot Format

    LeftRightDot format: Lowercase alphanumeric words separated by periods, with
    the most significant word (on the left) starting with an alphabet character.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not LeftRightDot format
    """
    try:
        x = v.split(".")
    except Exception as e:
        raise ValueError(f"Failed to seperate &lt;{v}> into words with split'.'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of &lt;{v}> must start with alphabet char."
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of &lt;{v}> split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of &lt;{v}> must be lowercase.")</xsl:text>

    </xsl:when>


    <xsl:when test="Name='LogStyleDateWithMillis'">
    <xsl:text>


def check_is_log_style_date_with_millis(v: str) -> None:
    """Checks LogStyleDateWithMillis format

    LogStyleDateWithMillis format:  YYYY-MM-DDTHH:mm:ss.SSS

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not LogStyleDateWithMillis format.
        In particular the milliseconds must have exactly 3 digits.
    """
    from datetime import datetime
    try:
        datetime.fromisoformat(v)
    except ValueError as e:
        raise ValueError(f"{v} is not in LogStyleDateWithMillis format") from e
    # The python fromisoformat allows for either 3 digits (milli) or 6 (micro)
    # after the final period. Make sure its 3
    milliseconds_part = v.split(".")[1]
    if len(milliseconds_part) != 3:
        raise ValueError(f"{v} is not in LogStyleDateWithMillis format."
                            " Milliseconds must have exactly 3 digits")
    </xsl:text>

    </xsl:when>




    <xsl:when test="Name='Near5'">
    <xsl:text>


def check_is_near5(v: str) -> None:
    """
    4.5 &lt;= v &lt;= 5.5
    """
    if v &lt; 4.5 or v > 5.5:
        raise ValueError(f"&lt;{v}> is not between 4.5 and 5.5, not Near5")</xsl:text>
    </xsl:when>

    <xsl:when test="Name='NonNegativeInteger'">
    <xsl:text>


def check_is_non_negative_integer(v: int) -> None:
    """
    Must be non-negative when interpreted as an integer. Interpretation
    as an integer follows the pydantic rules for this - which will round
    down rational numbers. So 0 is fine, and 1.7 will be interpreted as
    1 and is also fine.

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v &lt; 0
    """
    v2 = int(v)
    if v2 &lt; 0:
        raise ValueError(f"&lt;{v}> is not NonNegativeInteger")</xsl:text>
    </xsl:when>


    <xsl:when test="Name='PositiveInteger'">
    <xsl:text>


def check_is_positive_integer(v: int) -> None:
    """
    Must be positive when interpreted as an integer. Interpretation as an
    integer follows the pydantic rules for this - which will round down
    rational numbers. So 1.7 will be interpreted as 1 and is also fine,
    while 0.5 is interpreted as 0 and will raise an exception.

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v &lt; 1
    """
    v2 = int(v)
    if v2 &lt; 1:
        raise ValueError(f"&lt;{v}> is not PositiveInteger")</xsl:text>
    </xsl:when>

    <xsl:when test="Name='ReasonableUnixTimeMs'">
    <xsl:text>


def check_is_reasonable_unix_time_ms(v: int) -> None:
    """Checks ReasonableUnixTimeMs format

    ReasonableUnixTimeMs format: unix milliseconds between Jan 1 2000 and Jan 1 3000

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v is not ReasonableUnixTimeMs format
    """
    from datetime import datetime
    from datetime import timezone

    start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(3000, 1, 1, tzinfo=timezone.utc)

    start_timestamp_ms = int(start_date.timestamp() * 1000)
    end_timestamp_ms = int(end_date.timestamp() * 1000)

    if v &lt; start_timestamp_ms:
        raise ValueError(f"{v} must be after Jan 1 2000")
    if v > end_timestamp_ms:
        raise ValueError(f"{v} must be before Jan 1 3000")</xsl:text>


    </xsl:when>

    <xsl:when test="Name='ReasonableUnixTimeS'">
    <xsl:text>


def check_is_reasonable_unix_time_s(v: int) -> None:
    """Checks ReasonableUnixTimeS format

    ReasonableUnixTimeS format: unix seconds between Jan 1 2000 and Jan 1 3000

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v is not ReasonableUnixTimeS format
    """
    from datetime import datetime
    from datetime import timezone

    start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(3000, 1, 1, tzinfo=timezone.utc)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    if v &lt; start_timestamp:
        raise ValueError(f"{v} must be after Jan 1 2000")
    if v > end_timestamp:
        raise ValueError(f"{v} must be before Jan 1 3000")</xsl:text>

    </xsl:when>


    <xsl:when test="Name='SpaceheatName'">
    <xsl:text>


def check_is_spaceheat_name(v: str) -> None:
    """Check SpaceheatName Format.

    Validates if the provided string adheres to the SpaceheatName format:
    Lowercase alphanumeric words separated by hypens

    Args:
        candidate (str): The string to be validated.

    Raises:
        ValueError: If the provided string is not in SpaceheatName format.
    """
    try:
        x = v.split("-")
    except Exception as e:
        raise ValueError(f"Failed to seperate &lt;{v}> into words with split'-'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of &lt;{v}> must start with alphabet char."
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of &lt;{v}> split by by '-' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of &lt;{v}> must be lowercase.")</xsl:text>
    </xsl:when>


<xsl:when test="Name='HandleName'">
    <xsl:text>


def check_is_handle_name(v: str) -> None:
    """Check HandleName Format.

    Validates if the provided string adheres to the HandleName format:
    words separated by periods, where the worlds are lowercase alphanumeric plus hyphens

    Args:
        candidate (str): The string to be validated.

    Raises:
        ValueError: If the provided string is not in HandleName format.
    """
    try:
        x = v.split(".")
    except Exception as e:
        raise ValueError(f"Failed to seperate &lt;{v}> into words with split'.'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of &lt;{v}> must start with alphabet char."
        )
    for word in x:
        for char in word:
            if not (char.isalnum() or char == "-"):
                raise ValueError(
                    f"words of &lt;{v}> split by by '.' must be alphanumeric or hyphen."
                )
    if not v.islower():
        raise ValueError(f" &lt;{v}> must be lowercase.")</xsl:text>

    </xsl:when>
    <xsl:when test="Name='UuidCanonicalTextual'">
    <xsl:text>


def check_is_uuid_canonical_textual(v: str) -> None:
    """Checks UuidCanonicalTextual format

    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not UuidCanonicalTextual format
    """
    phi_fun_check_it_out = 5
    two_cubed_too_cute = 8
    bachets_fun_four = 4
    the_sublime_twelve = 12
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}") from e
    if len(x) != phi_fun_check_it_out:
        raise ValueError(f"&lt;{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError as e:
            raise ValueError(f"Words of &lt;{v}> are not all hex") from e
    if len(x[0]) != two_cubed_too_cute:
        raise ValueError(f"&lt;{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != bachets_fun_four:
        raise ValueError(f"&lt;{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != bachets_fun_four:
        raise ValueError(f"&lt;{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != bachets_fun_four:
        raise ValueError(f"&lt;{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != the_sublime_twelve:
        raise ValueError(f"&lt;{v}> word lengths not 8-4-4-4-12")</xsl:text>


    </xsl:when>

    <xsl:when test="Name='WorldInstanceNameFormat'">
    <xsl:text>


def check_is_world_instance_name_format(v: str) -> None:
    """Checks WorldInstanceName Format

    WorldInstanceName format: A single alphanumerical word starting
    with an alphabet char (the root GNodeAlias) and an integer,
    seperated by '__'. For example 'd1__1'

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not WorldInstanceNameFormat format
    """
    try:
        words = v.split("__")
    except Exception as e:
        raise ValueError(f"&lt;{v}> is not split by '__'") from e
    if len(words) != 2:
        raise ValueError(f"&lt;{v}> not 2 words separated by '__'")
    try:
        int(words[1])
    except Exception as e:
        raise ValueError(f"&lt;{v}> second word not an int") from e

    root_g_node_alias = words[0]
    first_char = root_g_node_alias[0]
    if not first_char.isalpha():
        raise ValueError(f"&lt;{v}> first word must be alph char")
    if not root_g_node_alias.isalnum():
        raise ValueError(f"&lt;{v}> first word must be alphanumeric")</xsl:text>
    </xsl:when>
    </xsl:choose>

</xsl:for-each>
</xsl:if>

<!-- Add newline at EOF for git and pre-commit-->
<xsl:text>&#10;</xsl:text>

                        </xsl:element>
                     </FileSetFile>
                </xsl:for-each>
                </xsl:for-each>
            </FileSetFiles>
        </FileSet>
    </xsl:template>


</xsl:stylesheet>
