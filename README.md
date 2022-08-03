# Metsenat
- database scheme: [link](https://drawsql.app/sevbo/diagrams/metsenant#)
- endpoints:
    <details>
    <summary>authentication</summary>
    <b>access token</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a style="color:skyblue">• POST /auth/login/</a><br>
    <b>refresh token</b>&nbsp;&nbsp;&nbsp;&nbsp;
    <a style="color:skyblue">• POST /auth/refresh/</a><br>
    <b>verify token</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a style="color:skyblue">• POST /auth/verify/</a>
    <pre>
    {
        "username": "string",
        "password": "string"
    }
    </pre>
    </details>
    <details>
    <summary>students</summary>
     <a style="color:skyblue">• POST &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/students/</a><br>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/students/</a><br>
     <a style="color:skyblue">• PUT &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/students/{student_id}/</a><br>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/students/{student_id}/sponsors/</a><br>
    </details>
    <details>
    <summary>sponsors</summary>
     <a style="color:skyblue">• POST &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/sponsors/</a><br>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/sponsors/</a><br>
     <a style="color:skyblue">• PUT &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/students/{sponsor_id}/</a><br>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/students/{sponsor_id}/sponsored/</a><br>
    </details>
    <details>
    <summary>sponsorship</summary>
     <a style="color:skyblue">• POST &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/sponsorships/</a><br>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/sponsorships/</a><br>
     <a style="color:skyblue">• PUT &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/sponsorship/{sponsorships_id}/</a><br>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/sponsorship/{sponsorships_id}/</a><br>
    </details>
    <details>
    <summary>dashboard</summary>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/dashboard/</a><br>
     <a style="color:skyblue">• GET &nbsp;&nbsp;&nbsp;&nbsp;/api/v1/dashboard/graph/</a><br>
    </details>

