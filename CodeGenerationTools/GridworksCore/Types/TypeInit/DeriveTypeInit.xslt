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
                    <xsl:element name="RelativePath"><xsl:text>../../../../src/gwproto/types/__init__.py</xsl:text></xsl:element>

                <OverwriteMode>Always</OverwriteMode>
                <xsl:element name="FileContents">
<xsl:text>
""" List of all the types """
</xsl:text>
<xsl:for-each select="$airtable//ProtocolTypes/ProtocolType[(normalize-space(ProtocolName) ='gwproto')]">
<xsl:sort select="VersionedTypeName" data-type="text"/>
<xsl:variable name="versioned-type-id" select="VersionedType"/>
<xsl:for-each select="$airtable//VersionedTypes/VersionedType[(VersionedTypeId = $versioned-type-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory = 'Json' or ProtocolCategory = 'GwAlgoSerial') and not (NotInInit='true')]">

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

<xsl:text>
from gwproto.types.</xsl:text>
<xsl:value-of select="translate(TypeName,'.','_')"/>
<xsl:text> import </xsl:text>
<xsl:value-of select="$python-class-name"/>
<xsl:text>
from gwproto.types.</xsl:text>
<xsl:value-of select="translate(TypeName,'.','_')"/>
<xsl:text> import </xsl:text><xsl:value-of select="$python-class-name"/>
<xsl:text>_Maker</xsl:text>
</xsl:for-each>
</xsl:for-each>
<xsl:text>


__all__ = [</xsl:text>
<xsl:for-each select="$airtable//ProtocolTypes/ProtocolType[(normalize-space(ProtocolName) ='gwproto')]">
<xsl:sort select="VersionedTypeName" data-type="text"/>
<xsl:variable name="versioned-type-id" select="VersionedType"/>
<xsl:for-each select="$airtable//VersionedTypes/VersionedType[(VersionedTypeId = $versioned-type-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory = 'Json' or ProtocolCategory = 'GwAlgoSerial')]">

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

<xsl:if test="not(NotInInit='true')">
<xsl:text>
    "</xsl:text>
</xsl:if>
<xsl:if test="(NotInInit='true')">
<xsl:text>
    # "</xsl:text>
</xsl:if>
    <xsl:value-of select="$python-class-name"/>
    <xsl:text>",</xsl:text>
<xsl:if test="not(NotInInit='true')">
<xsl:text>
    "</xsl:text>
</xsl:if>
<xsl:if test="(NotInInit='true')">
<xsl:text>
    # "</xsl:text>
</xsl:if>
    <xsl:value-of select="$python-class-name"/>
    <xsl:text>_Maker",</xsl:text>
</xsl:for-each>
</xsl:for-each>
<xsl:text>
]

</xsl:text>



                </xsl:element>
            </FileSetFile>


        </FileSet>
    </xsl:template>


</xsl:stylesheet>
