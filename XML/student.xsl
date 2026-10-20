
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
        <body>
            <h2>Student Details</h2>

            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Roll Number</th>
                    <th>Name</th>
                    <th>Year</th>
                    <th>Email</th>
                    <th>Marks</th>
                </tr>

                <xsl:for-each select="studman/student">
                    <tr>
                        <td><xsl:value-of select="@id"/></td>
                        <td><xsl:value-of select="rollno"/></td>
                        <td><xsl:value-of select="name"/></td>
                        <td><xsl:value-of select="year"/></td>
                        <td><xsl:value-of select="email"/></td>
                        <td><xsl:value-of select="marks"/></td>
                    </tr>
                </xsl:for-each>

            </table>
        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
//python -c "from lxml import etree; x=etree.parse('demo.xml'); s=etree.XSLT(etree.parse('student.xsl')); open('output.html','wb').write(etree.tostring(s(x),method='html',pretty_print=True))"
//start .\output.html