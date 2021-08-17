<h2>kivy and parellel programming between mainthread(kivy) and other threads</h2>


<p> When is starting any kivy app, there is a main loop that is running during the whole lifecycle of the your appplication.<br>
  that main loop is single-threaded. This can cause problems when building callbacks with infinite loop(e.g. while True:) <br>
  inside the main loop. Usually, the main loop is broken and your application doesn't work anymore
</p>
