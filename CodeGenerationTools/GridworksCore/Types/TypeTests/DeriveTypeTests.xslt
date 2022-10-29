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
                <xsl:for-each select="$airtable//Schemas/Schema[(normalize-space(Alias) !='')  and (InGwProto = 'true') and (Status = 'Active' or Status = 'Pending') and (ProtocolType = 'Json')]">
                    <xsl:variable name="alias" select="AliasRoot"/>
                    <xsl:variable name="schema-id" select="SchemaId" />  
                    <xsl:variable name="local-alias" select="AliasRoot" />  
                    <xsl:variable name="class-name">
                        <xsl:call-template name="nt-case">
                            <xsl:with-param name="mp-schema-text" select="$local-alias" />
                        </xsl:call-template>
                    </xsl:variable>
                    <xsl:variable name="python-data-class">
                        <xsl:call-template name="python-case">
                            <xsl:with-param name="camel-case-text" select="translate(DataClass,'.','_')"  />
                        </xsl:call-template>
                    </xsl:variable>
                    <xsl:variable name="data-class-id">
                        <xsl:if test="IsCac='true'">
                            <xsl:text>component_attribute_class_id</xsl:text>
                        </xsl:if>
                        <xsl:if test="IsComponent='true'">
                            <xsl:text>component_id</xsl:text>
                        </xsl:if>
                        
                        <xsl:if test="not (IsCac='true') and not (IsComponent='true')">
                            <xsl:value-of select="$python-data-class"/><xsl:text>_id</xsl:text>
                       </xsl:if>
                    </xsl:variable>
                    <FileSetFile>
                                <xsl:element name="RelativePath"><xsl:text>../../../../tests/gt/test_</xsl:text>
                                <xsl:value-of select="translate($local-alias,'.','_')"/><xsl:text>.py</xsl:text></xsl:element>

                        <OverwriteMode>Always</OverwriteMode>
                        <xsl:element name="FileContents">

   
<xsl:text>"""Tests </xsl:text><xsl:value-of select="AliasRoot"/><xsl:text> type"""
import json
import pytest
from pydantic import ValidationError
from gwproto import Message</xsl:text>
<xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
<xsl:if test="IsEnum = 'true'">
<xsl:text>
from gwproto.enums import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
</xsl:call-template>
</xsl:if>
</xsl:for-each>
<xsl:text>
from gwproto.errors import SchemaError
from gwproto.messages import </xsl:text>
<xsl:value-of select="$class-name"/><xsl:text>
from gwproto.messages import </xsl:text>
<xsl:value-of select="$class-name"/><xsl:text>_Maker as Maker


def test_</xsl:text><xsl:value-of select="translate($local-alias,'.','_')"/>
<xsl:text>_generated():

    d = {</xsl:text>
        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and ((not (IsEnum = 'true') and normalize-space(SubTypeDataClass) = '') or (IsList = 'true'))]">
        <xsl:text>
        "</xsl:text><xsl:value-of select="Value"  />
        <xsl:text>": </xsl:text>
        <xsl:value-of select="normalize-space(TestValue)"/>
        <xsl:text>,</xsl:text>
        </xsl:for-each>
        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and (IsEnum = 'true') and not (IsList = 'true')]">
        <xsl:text>
        "</xsl:text><xsl:value-of select="Value"  />
        <xsl:text>GtEnumSymbol": </xsl:text>
        <xsl:value-of select="normalize-space(TestValue)"/>
            <xsl:text>,</xsl:text>
        </xsl:for-each>

        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and (normalize-space(SubTypeDataClass) != '')and  not (IsList = 'true')]">
        <xsl:text>
        "</xsl:text><xsl:value-of select="Value"  />
        <xsl:text>Id": </xsl:text>
        <xsl:value-of select="normalize-space(TestValue)"/>
        <xsl:text>,</xsl:text>
        </xsl:for-each>
    <xsl:text>
        "TypeAlias": "</xsl:text><xsl:value-of select="$alias"/><xsl:text>",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gw_type = json.dumps(d)
    gw_tuple = Maker.type_to_tuple(gw_type)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple

    # test Maker init
    payload = Maker(
        </xsl:text>
        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
        <xsl:if test="(normalize-space(SubTypeDataClass) = '') ">
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>=gw_tuple.</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>,
        </xsl:text>
        </xsl:if>
        <xsl:if test="(normalize-space(SubTypeDataClass) != '') ">
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>_id=gw_tuple.</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>Id,
        </xsl:text>
        </xsl:if>
        </xsl:for-each>
        <xsl:text>#
    ).tuple
    assert payload == gw_tuple
</xsl:text>


    <xsl:if test="MakeDataClass='true'">
    <xsl:text>
    ######################################
    # Dataclass related tests
    ######################################

    dc = Maker.tuple_to_dc(gw_tuple)
    assert gw_tuple == Maker.dc_to_tuple(dc)
    assert Maker.type_to_dc(Maker.dc_to_type(dc)) == dc

        </xsl:text>
    </xsl:if>


<xsl:text>
    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)</xsl:text>

    <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and (IsRequired='true') ]">

    
    <xsl:if test = "((not (IsEnum = 'true') and normalize-space(SubTypeDataClass) = '') or (IsList = 'true'))">
    <xsl:text>

    d2 = dict(d)
    del d2["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>"]
    with pytest.raises(ValidationError):
        </xsl:text><xsl:value-of select="$class-name"/><xsl:text>(**d2)</xsl:text>
    </xsl:if>

    <xsl:if test = "(IsType = 'true')">
    <xsl:text>

    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)</xsl:text>

    </xsl:if>

    <xsl:if test = "((IsEnum = 'true') and not (IsList = 'true'))">
    <xsl:text>
   
    d2 = dict(d)
    del d2["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>GtEnumSymbol"]
    with pytest.raises(ValidationError):
        </xsl:text><xsl:value-of select="$class-name"/><xsl:text>(**d2)

    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)</xsl:text>
    </xsl:if>


    <xsl:if test = "((normalize-space(SubTypeDataClass) != '') and not (IsList = 'true'))">
    <xsl:text>orig_value = d["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>Id"]
    del d["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>Id"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["</xsl:text><xsl:value-of  select="Value"/>
    <xsl:text>Id"] = orig_value

    </xsl:text>
    </xsl:if>
    
    </xsl:for-each>

    <xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and not (IsRequired='true')]) > 0">
    <xsl:text>

    ######################################
    # Optional attributes can be removed from type
    ######################################

    </xsl:text>
    <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and not (IsRequired='true')]">
    <xsl:if test= "(normalize-space(SubTypeDataClass) != '')">
    <xsl:text>orig_value = d["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>Id"]
    del d["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>Id"]
    gw_type = json.dumps(d)
    gw_tuple = Maker.type_to_tuple(gw_type)
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple
    d["</xsl:text><xsl:value-of  select="Value"/>
    <xsl:text>Id"] = orig_value

    </xsl:text>
    </xsl:if>
    <xsl:if  test= "(normalize-space(SubTypeDataClass) = '')">
    <xsl:text>orig_value = d["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>"]
    del d["</xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>"]
    gw_type = json.dumps(d)
    gw_tuple = Maker.type_to_tuple(gw_type)
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple
    d["</xsl:text><xsl:value-of  select="Value"/>
    <xsl:text>"] = orig_value

    </xsl:text>
    </xsl:if>
    </xsl:for-each>
    </xsl:if>
    <xsl:text>
    ######################################
    # Behavior on attribute types
    ######################################

    </xsl:text>
    <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
    <xsl:variable name="attribute"><xsl:value-of select="Value"/></xsl:variable>



    <xsl:if test = "(normalize-space(SubTypeDataClass) != '')">
        <xsl:text>orig_value = d["</xsl:text>
        <xsl:value-of  select="Value"/><xsl:text>Id"]
    d["</xsl:text><xsl:value-of  select="Value"/><xsl:text>Id"] = "Not a dataclass id"
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d)
    d["</xsl:text><xsl:value-of  select="Value"/><xsl:text>Id"] = orig_value

    </xsl:text>
    </xsl:if>



    <xsl:if test= "not(IsList = 'true') and (IsType='true') and (normalize-space(SubTypeDataClass) = '') ">
    <xsl:text>d2 = dict(d, </xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>="Not a </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
    </xsl:call-template><xsl:text>.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    </xsl:text>
    </xsl:if>



    <xsl:if test= "not(IsList = 'true') and (IsPrimitive='true') ">
    
    <xsl:text>d2 = dict(d, </xsl:text>
    <xsl:value-of  select="Value"/><xsl:text>=</xsl:text>
            <xsl:if test = "PrimitiveType='Integer'">
            <xsl:text>"</xsl:text>
            <xsl:value-of select="normalize-space(TestValue)"/>
            <xsl:text>.1"</xsl:text>
            </xsl:if>
            <xsl:if test = "PrimitiveType='Number'">
            <xsl:text>"This string is not a float."</xsl:text>
            </xsl:if>
            <xsl:if test = "PrimitiveType='Boolean'">
            <xsl:text>"This string is not a boolean."</xsl:text>
            </xsl:if>
            <xsl:if test = "PrimitiveType='String'">
            <xsl:text>{}</xsl:text>
            </xsl:if>
    
    <xsl:text>)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    </xsl:text>
    <xsl:if test = "PrimitiveType='Integer'">
    <xsl:text>d2 = dict(d, </xsl:text>
    <xsl:value-of select="Value"/><xsl:text>="</xsl:text>
    <xsl:value-of select="normalize-space(TestValue)"/>
    <xsl:text>")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, </xsl:text>
    <xsl:value-of select="Value"/><xsl:text>=</xsl:text>
    <xsl:value-of select="normalize-space(TestValue)"/>
    <xsl:text>.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    </xsl:text>
    </xsl:if>
    </xsl:if>



    <xsl:if test = "not (IsList = 'true') and IsEnum = 'true'">
    
    <xsl:text>d2 = dict(d, </xsl:text>
     <xsl:value-of  select="Value"/><xsl:text>GtEnumSymbol="Unrecognized enum symbol")
    assert Maker.dict_to_tuple(d2).</xsl:text>
    <xsl:value-of  select="Value"/>
    <xsl:text> == </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template>
    <xsl:text>.UNKNOWN

    </xsl:text>

    </xsl:if>



    <xsl:if test= "(IsList = 'true') and (IsType='true') ">
    <xsl:text>d2 = dict(d, </xsl:text>
    <xsl:value-of  select="Value"/>
    <xsl:text>= "Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, </xsl:text>
        <xsl:value-of  select="Value"/>
        <xsl:text> = ["Not even a dict"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, </xsl:text>
        <xsl:value-of  select="Value"/>
        <xsl:text> = [{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    </xsl:text>
    </xsl:if>



    <xsl:if test = "(IsList = 'true') and (IsPrimitive = 'true')">
        <xsl:text>d2 = dict(d, </xsl:text>
        <xsl:value-of  select="Value"/><xsl:text>=</xsl:text>
                <xsl:if test = "PrimitiveType='Integer'">
            <xsl:text>["1.1"])
    </xsl:text>
                </xsl:if>
                <xsl:if test = "PrimitiveType='Number'">
            <xsl:text>["This string is not a float."])
    </xsl:text>
                </xsl:if>
                <xsl:if test = "PrimitiveType='Boolean'">
            <xsl:text>["This string is not a boolean."])
    </xsl:text>
                </xsl:if>
                <xsl:if test = "PrimitiveType='String'">
            <xsl:text>[{}])
    </xsl:text>
                </xsl:if>

        <xsl:text>with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    </xsl:text>
    </xsl:if>



    <xsl:if test = "(IsList = 'true') and (IsEnum= 'true')">

    <xsl:text>d2 = dict(d, </xsl:text>
    <xsl:value-of select="Value"/>
    <xsl:text>=["Unrecognized enum symbol"])
    assert Maker.dict_to_tuple(d2).</xsl:text>
    <xsl:value-of select="Value"/>
    <xsl:text> == [</xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template>
    <xsl:text>.UNKNOWN]

    </xsl:text>
    </xsl:if>
    

    </xsl:for-each>

    <xsl:text>######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
</xsl:text>    
    <xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and (normalize-space(PrimitiveFormatFail1) != '')]) > 0">

<xsl:text>
    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################</xsl:text>

    <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and (normalize-space(PrimitiveFormatFail1) != '')]">
    
    <xsl:if test="not(IsList = 'true')">
    <xsl:text>

    d2 = dict(d, </xsl:text>
    <xsl:value-of select="Value"/>
    <xsl:text>=</xsl:text>
    <xsl:value-of select="normalize-space(PrimitiveFormatFail1)"/><xsl:text>)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)</xsl:text>
    </xsl:if>


    <xsl:if test="IsList = 'true'">
    <xsl:text>

    d2 = dict(d, </xsl:text>
    <xsl:value-of select="Value"/>
    <xsl:text>=[</xsl:text>
    <xsl:value-of select="normalize-space(PrimitiveFormatFail1)"/><xsl:text>])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)</xsl:text>
        </xsl:if>
    </xsl:for-each>

    <xsl:text>

    # End of Test
</xsl:text>
</xsl:if>

    


                        </xsl:element>
                     </FileSetFile>
                </xsl:for-each>

            </FileSetFiles>
        </FileSet>
    </xsl:template>


</xsl:stylesheet>