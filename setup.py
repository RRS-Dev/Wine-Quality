import setuptools

with open('Readme.md','r',encoding='utf-8') as f:
    long_description = f.read()



__version__ = '0.0.0'

repo_name = 'ML-Project-END-to-END'
author_username = 'RRS-Dev'
SRC_repo = 'Wine_Quality'
author_email = 'srivastavaraj1313@gmail.com'

setuptools.setup(
    name=SRC_repo,
    version=__version__,
    author=author_username,
    author_email=author_email,
    description='Small ML package',
    long_description=long_description,
    long_description_content = 'text/markdown',
    url = f'https://github.com/{author_username}/{repo_name}',
    project_urls = {
        "Bug Tracker":f'https://github.com/{author_username}/{repo_name}/issues'
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)


