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

            <FileSetFile>
                    <xsl:element name="RelativePath"><xsl:text>../../../../src/gwproto/gt/__init__.py</xsl:text></xsl:element>

                <OverwriteMode>Always</OverwriteMode>
                <xsl:element name="FileContents">
<xsl:text>
""" List of all the gt types """
</xsl:text>
<xsl:for-each select="$airtable//Schemas/Schema[(normalize-space(Alias) !='')  and (InGwProto = 'true') and (Status = 'Active' or Status = 'Pending') and (ProtocolType = 'Json')]">
<xsl:text>
from .</xsl:text>
<xsl:value-of select="translate(AliasRoot,'.','_')"/>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="mp-schema-text" select="AliasRoot" />
</xsl:call-template>
</xsl:for-each>
<xsl:text>

__all__ = [</xsl:text>
<xsl:for-each select="$airtable//Schemas/Schema[(normalize-space(Alias) !='')  and (InGwProto = 'true') and (Status = 'Active' or Status = 'Pending') and (ProtocolType = 'Json')]">
<xsl:text>
    "</xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="AliasRoot" />
    </xsl:call-template>
    <xsl:text>",</xsl:text>
</xsl:for-each>
<xsl:text>
]
    
</xsl:text>



                </xsl:element>
            </FileSetFile>


        </FileSet>
    </xsl:template>


</xsl:stylesheet>