# 🦄 Generate .npmrc file for Azure DevOps

This github action generates a .npmrc file for Azure DevOps

```yaml
- uses: ponicode/azure-devops-npm-action@master
  with:
    organisation: "Ponicode"
    project: "my_project"
    registry: "my_registry"
    user: "unicorn"
    password: "myPasswordIsASecret"
    email: "unicorn@ponicode.com"
    scope: "@ponicode"
```

# Ponicode Action inputs

| Name           | Description               | Required |
| -------------- | ------------------------- | -------- | 
| `organisation` | Your Azure organisation   | true     |
| `project`      | Your Azure project        | true     |
| `registry`     | Your Azure registry       | false    | 
| `user`         | Your Azure user           | false    | 
| `password `    | Your Azure password       | false    | 
| `email`        | Your Azure email          | false    | 
| `scope`        | Your Azure scope          | false    | 

We would love to hear your feedback! Tell us what you loved and what you want us to improve about this action at feedback@ponicode.com, or feel free to open a Github Issue.<br />
We also have a [Slack community channel](https://ponicode-community.slack.com/join/shared_invite/zt-fiq4fhkg-DE~a_FkJ7xtiZxW7efyA4Q#/), where people can ask for help if they encounter problems with our products and where we keep you informed about our latest releases.<br />
If you want to know more about Ponicode and the different services we propose, check out our website [www.ponicode.com](https://ponicode.com)! <br /> <br/>
<img alt="Ponicode Logo" src="https://avatars0.githubusercontent.com/u/49948625?s=200&v=4=200zx" width="100"/>
