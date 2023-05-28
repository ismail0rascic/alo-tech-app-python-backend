<h2>AloTech Spotify tracker</h2>

Tracks App This is a web application that allows users to search for popular tracks based on music genres. It utilizes the Spotify API to retrieve information about artists and their popular tracks.
 
<h3>First version</h3>
Full version of app with frontend you can find a this link:https://github.com/ismail0rascic/alo-tech-app
This is just backend with all same options like on provided link but instead of NodeJs this solution is coded in Python Flask


<h3>GoogleCloud</h3>
  App is depoloyed on Google Cloud Run, to acces folow next link :
  <li>SERVER: https://python-server-5fjjz6ugna-ue.a.run.app/</li>
  
  
<h3>For starting App on owen PC follow next steps</h3>
<ol>
<li>Crate folder in which you want place code (you use -mkdir- command)</li>
<li>Access folder  -cd + folder path- </li>
<li>Use  -git clone + link of this repository-</li>
<li>Create .env file and set CLIENT_ID and CLIENT_SECRET </li>
<li>Run next commands:</li>
   <ul>
    <li>python -m venv venv</li>
    <li>.\venv\Scripts\activate</li>
    <li>pip install -r requirements.txt</li>
   </ul>
<li>Start app</li>
 <ul>
    <li>For development mode run : python app.py (default port 5000)</li>
    <li>For production mode run: python wsgi.py (default port 8080)</li>   
 </ul>
  <ol>
