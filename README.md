
# Sphinx Template

This Repo contains a Template for creating a sphinx project. It also offers some scripts to build and serve the documentation over a local http server. It was mainly created as a personal project to provide a fast way to create a new documentation & save some tools 
for creating the documentation.

## Usage

Clone this repo where the documentation shall live.

```bash
git clone https://github.com/BNieser/sphinx_template.git
```

go into cloned folder 

```bash
    cd sphinx_template
```


Install dependencies or add them to your `pyproject.toml`




Remove the `.git` file to add it to your repo.

```bash
rm -rf .git
```


## serving over http for Linux

in [scripts](scripts/) there is a small script which provides the build HTML documentation 
over a local http server. 

You can start it with 

```bash
./scripts/provide.py
```

When you have updated the documentation you only have to rebuild the HTML docs 


go in to the folder where the makefile is located and execute 

```bash
make html
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
