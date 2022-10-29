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
                <xsl:for-each select="$airtable//GtEnums/GtEnum[(normalize-space(Alias) !='' and Status='Active')]">
                    <xsl:variable name="enum-alias" select="Alias" />  
                    <xsl:variable name="enum-name-style" select="PythonEnumNameStyle" /> 
                    <xsl:variable name="class-name">
                        <xsl:call-template name="nt-case">
                            <xsl:with-param name="mp-schema-text" select="Alias" />
                        </xsl:call-template>
                    </xsl:variable>
                    <xsl:variable name="local-class-name">
                        <xsl:call-template name="nt-case">
                            <xsl:with-param name="mp-schema-text" select="LocalName" />
                        </xsl:call-template>
                    </xsl:variable>
                    <xsl:variable name="enum-id" select="GtEnumId"/>
                    <FileSetFile>
                                <xsl:element name="RelativePath"><xsl:text>../../../src/gwproto/enums/</xsl:text>
                                <xsl:value-of select="translate(Alias,'.','_')"/><xsl:text>.py</xsl:text></xsl:element>

                        <OverwriteMode>Always</OverwriteMode>
                        <xsl:element name="FileContents">

   
<xsl:text>"""Schema enum </xsl:text><xsl:value-of select="$enum-alias"/><xsl:text> definition.

Look in enums/</xsl:text><xsl:value-of select="translate(Alias,'.','_')"/><xsl:text> for:
    - the local python enum </xsl:text><xsl:value-of select="$local-class-name"/><xsl:text>
    - the SchemaEnum </xsl:text><xsl:value-of select="$class-name"/>SchemaEnum<xsl:text>

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from typing import Dict
from enum import auto
from fastapi_utils.enums import StrEnum
from abc import ABC
from typing import List
from gwproto.errors import SchemaError


class </xsl:text><xsl:value-of select="$local-class-name"/>
<xsl:text>(StrEnum):
    """
    </xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
    <xsl:value-of select="LocalValue"/>
    <xsl:text>,
    </xsl:text>
    </xsl:for-each>
    <xsl:text>
    This is the enum intended for the local application. It is forwards and backwards
    compatible with </xsl:text><xsl:value-of select="$local-class-name"/>
    <xsl:text> enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    </xsl:text> 

<xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
<xsl:value-of select="LocalValue"/>
<xsl:text> = auto()
    </xsl:text>
    </xsl:for-each>
<xsl:text>


class </xsl:text><xsl:value-of select="$local-class-name"/><xsl:text>Map:
    """ Handles the bijection</xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
        <xsl:text>
        "</xsl:text><xsl:value-of select="Symbol"/><xsl:text>" -  </xsl:text>
        <xsl:value-of select="LocalValue"/>
    <xsl:text>,</xsl:text>
    </xsl:for-each>
    <xsl:text>
    """
    type_name = "</xsl:text>
<xsl:value-of select="$enum-alias"/>

    <xsl:text>"

    symbols: List[str] = [
        </xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
    <xsl:text>"</xsl:text><xsl:value-of select="Symbol"/><xsl:text>",
        </xsl:text>
</xsl:for-each>
<xsl:text>#
    ]

    @classmethod
    def is_symbol(cls, candidate) -> bool:
        if candidate in cls.symbols:
            return True
        return False

    @classmethod
    def type_to_local(cls, symbol):
        if not cls.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to key of {</xsl:text><xsl:value-of select="$local-class-name"/>
                <xsl:text>Map.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, </xsl:text>
            <xsl:value-of select="translate(LocalName,'.','_')"/><xsl:text>):
        if not isinstance(</xsl:text><xsl:value-of select="translate(LocalName,'.','_')"/><xsl:text>, </xsl:text>
        <xsl:value-of select="$local-class-name"/><xsl:text>):
            raise SchemaError(f"{</xsl:text>
                <xsl:value-of select="translate(LocalName,'.','_')"/><xsl:text>} must be of type {</xsl:text>
                    <xsl:value-of select="$local-class-name"/><xsl:text>}")
        return cls.local_to_type_dict[</xsl:text>
        <xsl:value-of select="translate(LocalName,'.','_')"/><xsl:text>]

    type_to_local_dict: Dict[str, </xsl:text><xsl:value-of select="$local-class-name"/><xsl:text>] = {</xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
        <xsl:text>
        "</xsl:text><xsl:value-of select="Symbol"/><xsl:text>": </xsl:text>
        <xsl:value-of select="$local-class-name"/><xsl:text>.</xsl:text>
        <xsl:value-of select="LocalValue"/>
    <xsl:text>,</xsl:text>
    </xsl:for-each>
    <xsl:text>
    }

    local_to_type_dict: Dict[</xsl:text><xsl:value-of select="$local-class-name"/><xsl:text>, str] = {
        </xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
    <xsl:value-of select="$local-class-name"/><xsl:text>.</xsl:text>
    <xsl:value-of select="LocalValue"/>
    <xsl:text>: "</xsl:text>
    <xsl:value-of select="Symbol"/><xsl:text>",
        </xsl:text>
    </xsl:for-each>
    <xsl:text>#
    }
</xsl:text>


                        </xsl:element>
                     </FileSetFile>
                </xsl:for-each>

            </FileSetFiles>
        </FileSet>
    </xsl:template>


</xsl:stylesheet>