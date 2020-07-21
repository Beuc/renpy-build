from renpybuild.model import task

version = "1.6.37"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libpng-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("libpng-{{version}}")

    c.update_config_sub()

    c.run("""{{ configure }} {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""{{ make }} install """)
