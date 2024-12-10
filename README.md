<p>Im working on this personal project about administrative management that handle a specific logic of business and a excelent manage of countable stuff for your business, im trying to make this SaaS for personal training and deeply understanding of the concept Server-Client.</p>

***This is an API Project made on Django-rest***

The Dependencies i use on this Project are:

<li>djangorestframework</li>
<li>pillow</li>
<li>PyMySQL</li>
<li>python-decouple</li>
<li>pandas</li>
<li>numpy</li>
<li>django-jazzmin</li>
<li>cryptography</li>





***<h1>End-Points</h1>***
<h1>api/lista/distribuidores</h1>

<p>
  this endpoint is for a get request, returning all the Distribuidores models objects that are listed on the database.
</p>


<h1>'api/editar-distribuidores/<int:pk>/'</h1>

<p>
  this endpoint is for a Put request with the id of the instance that u wanna edit, if the ID is valid you will get the object that you edited as Response.
</p>

<h1>api/crear-nuevos-distribuidores/</h1>

<p>
  this endpoint is for Post request, this endpoint handle the creation of a new instanse on the Distribuidores Model, as the other ones that are not created yet like Distribuidor and, Producto, you can create all those Models instances or choose one that are allready created.
</p>

<h1>api/lista/distribuidor</h1>

<p>
  this endpoint is for a get request, returning all the Distribuidor models objects that are listed on the database.
</p>

<h1>api/crear-nuevo-distribuidor/</h1>

<p>
  This endpoint is for Post request and create a new instance of a Distribuidor.
</p>


<h1>'editar-distriubidor/<int:pk>/'</h1>

<p>
  this endpoint is for a Put request with the id of the instance that u wanna edit, if the ID is valid you will get the object that you edited as Response.
</p>

  
