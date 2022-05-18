<ul>

  <h1>Eletronic Invoice Automation</h1>


  <li>
    <h2>About this project</h2>
  
    This application aims to automate electronic invoice processing and issuance. 
    It reads an excel file that contains the clients required commercial information.
    Then, it takes the data to fill up a form on an electronic invoice processing website.
    At last, it generates and downloads the invoice of each client .
    All this process happens automatically!
 </li>
  
  <br>
  
  <li>
  <h3> Technologies </h3>
  This project's been developed using the following technologies:<br>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://selenium-python.readthedocs.io//">Selenium</a></li>
    <li><a href="https://chromedriver.chromium.org/home">Chrome Driver</a></li>
    <li><a href="https://pandas.pydata.org/">Pandas </a></li>
  </ul>
  </li>
  
  <br>
  
  <li>
    <h2>Setup</h2> 
    <ol>
      <li> First, check if you have <b>Python</b> and <b>pip</b> properly installed in your environment;</li><br>
      <li> 
        Then, install the required packages running the following command:<br><br>
        * If you would like, you can use a virtual environment to install them, like virtualenv or pipenv
                
        $ pip install -r requirements.txt
   </li>
      <li> To finish the setup, follow the .env.example file and create a file .env </li><br>
      <li> Next, declare the required variables (login and password).</li><br>
  </ol>
  </li>
  
  <li>
    <h2>Running the application</h2> 
    <ol>
      <li> 
        In the directory, run the following command:<br><br>
                
        $ python run.py
   </li>
   <br>
   <li> Once the application is running it will be possible to keep up with the Selenium browser </li><br>
   <li> So, you can check the eletronic invoices been processed automaticaly</li><br>
   <li> It will fill the form in the website with the desired inputs</li><br>
   <li> After that, it will download the e-invoice of each client to the desired folder in your system.</li><br>
  </ol>
  </li>
  
  
</ul>

<h3>This project is under improvement. Feel free to contribute with new ideas! :octocat:</h3>

