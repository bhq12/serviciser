Ideas:

///////////////////
FEATURE: SUPPORT CUSTOM LIBRARIES AND CLI PATHWAYS
//////////////////

- Support for config files:
    - Question/Answer pointers to directories
    - Some kind of DAG?
    - Q's and A's probably need a parent/child hierarchy to traverse

- Support for custom libraries:
    - Ability to point at custom templates zip/directory
    - Point at a URL for hosted template packages?

- Suppose the library would have the config file located at the root directory

- Above configured via environment variables?
    - e.g.:
        - process.env.SERVICISER_PACKAGE_LOCATION
        - If SERVICISER_PACKAGE_LOCATION is not set, use default templates


///////////////////
FEATURE: SUPPORT TEMPLATING INSIDE TEMPLATES
//////////////////

- Eg {{ app-name }}

- Jinja templating would make sense seeing the CLI is python
- Need some way of ensuring we don't conflict with and other jinja templating used in template libraries
- Idea:
    - Use prefix for serviciser jinja template variables:
        - e.g.: {{ serviciser.app-name }}
