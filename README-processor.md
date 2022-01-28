[![License](http://img.shields.io/:license-mit-blue.svg?style=flat)](https://opensource.org/licenses/MIT)

# Vision

### Description
Vision is an image stream processing engine built on top of Faust (stream processing library).
Use the application to process images at scale and in real-time.

#### Agents
Use agents to create a workflow. Workflow is an ordered list of processing to apply on a image. Processor input schema consist of workflow and image data (ndarray converted to list).

 - agent_transformer_color_bgr2gray
 - agent_save_to_disk
 - agent_filter_object_detection (TODO)
 
#### Features (being considered):
 - object detection
 - classify images
 - understand text
 - detect emotion
 - label images
 - build metadata

### Benchmarks
This is very early in development process for any benchmark (for realtime, etc.) Dates are being discussed for an alpha release. 

### Demos
This is very early in development process for any demos. Dates are being discussed for an alpha release. 

### Resources
- documentation
- samples

## Developer section

#### Platform/language version supported
Application is written on python and supports 3.8 and above.
Main branch will be the only official branch for now as this project is in active development.
The repo is in active maintenance.

#### 3rd party libraries used
- faust (link)

#### Branch info
- main branch

#### Repo status
Under active development

## Similar tools
Aim is to make alternative to google vision api where we can process image in scale and use many processors to gain valuable insights.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Support + Feedback](#support--feedback)
- [Vulnerability Reporting](#vulnerability-reporting)
- [Thank You](#thank-you)
- [What is Auth0](#what-is-auth0)
- [License](#license)

## Documentation

This section should describe the documentation contained within this repo as well as links to other helpful pages. Full documentation for the library should not, ideally, be located in the repo README and must not be duplicated from somewhere else. If the README is being updated to adhere to these guidelines and the documentation only exists in the readme, consider moving it to a docs page or a Quickstart.

Consider adding:

- How to generate documentation in the project (if applicable)
- Links to Quickstarts and sample projects
- Links to any specific `.md` files in the repo
- Links to [auth0/docs](https://auth0.com/docs/)
- Links to [Auth0 blog posts](https://auth0.com/blog/tech/)
- Links to any helpful supporting information about the project
- Links to relevant Community posts (consider parsing and adding somewhere more easily accessible)

## Installation

This section should outline what is required to install and configure this project. Consider adding:

- Prerequisites for use
- Command line instructions using `bash` syntax:

```bash
npm install
composer install
```

- Links to information about package manager used
- Information about `.env` values needed (include an `example.env` file)
- Include different ways to install, indicate preferred method
- Include instructions on how to install older versions

## Getting Started

This section should include basic usage instructions that can be successfully completed after [Installation](#installation) above. This section should be a short introduction to how this library can be used, not a duplication of existing Quickstarts.

Consider adding:

- Working with the Authentication API
	- Basic login
	- Basic code exchange
	- Authorize redirect
	- Logout
- Working with the Management API
	- Perform a Client Credentials grant
	- Get Users by page
	- Get Clients by page
	- Get Connections by page
- Other common tasks
- Security recommendations
	- State validation
	- ID token verification

## Contributing

We appreciate feedback and contribution to this repo! Before you get started, please see the following:

- [Auth0's general contribution guidelines](https://github.com/auth0/open-source-template/blob/master/GENERAL-CONTRIBUTING.md)
- [Auth0's code of conduct guidelines](https://github.com/auth0/open-source-template/blob/master/CODE-OF-CONDUCT.md)
- [This repo's contribution guide](CONTRIBUTING.md)

## Support + Feedback

Include information on how to get support. Consider adding:

- Use [Issues](https://github.com/auth0/open-source-template/issues) for code-level support
- Use [Community](https://community.auth0.com/) for usage, questions, specific cases
- Link to other support forums and FAQs

## Vulnerability Reporting

Please do not report security vulnerabilities on the public GitHub issue tracker. The [Responsible Disclosure Program](https://auth0.com/whitehat) details the procedure for disclosing security issues.

## What is Auth0?

Auth0 helps you to easily:

- implement authentication with multiple identity providers, including social (e.g., Google, Facebook, Microsoft, LinkedIn, GitHub, Twitter, etc), or enterprise (e.g., Windows Azure AD, Google Apps, Active Directory, ADFS, SAML, etc.)
- log in users with username/password databases, passwordless, or multi-factor authentication
- link multiple user accounts together
- generate signed JSON Web Tokens to authorize your API calls and flow the user identity securely
- access demographics and analytics detailing how, when, and where users are logging in
- enrich user profiles from other data sources using customizable JavaScript rules

[Why Auth0?](https://auth0.com/why-auth0)

## Thank You! (optional)

Information on the dependencies used, if desired.

## License

Link to [LICENSE](LICENSE) doc. Typically MIT but can be different for a specific platform.