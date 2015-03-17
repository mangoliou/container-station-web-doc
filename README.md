# container-station-web-doc

In **conf.py**, comment the following lines, and disable **runcode** module in extension.:

> import sphinx_rtd_theme <br>
> sys.path.insert(0, os.getcwd() + '/../ctstation/') <br>
> sys.path.insert(1, os.getcwd() + '/../doc/') <br>
> html_theme = "sphinx_rtd_theme" <br>
> html_theme_path = [sphinx_rtd_theme.get_html_theme_path()] <br>


In **index.rst** ,replace version with runcode part and add '_' to each file.

Then run:
> python trim.py
