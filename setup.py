from setuptools import setup, find_packages

setup(
    name='ajex_integration',
    version='0.0.1',
    description='ERPNext AJEX Integration',
    author='Nasiruddin Ansari',
    author_email='you@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"]
)
