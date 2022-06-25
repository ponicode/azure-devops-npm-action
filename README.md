# 🦄 Generate .npmrc file for Azure DevOps

This github action generates a `.npmrc` file for Azure DevOps

```yaml
- uses: ponicode/azure-devops-npm-action@master
  with:
    organisation: "Ponicode"
    project: "my_project"
    registry: "my_registry"
    user: "unicorn"
    password: ${{ secrets.AZURE_TOKEN }}
    email: "unicorn@ponicode.com"
    scope: "ponicode"
```
# How to setup (You must follow steps 1 and 2 to make the action work)
## **Step 1**: Create a yaml workflow file in your project
Go to the root of your project, and create the path to your workflow file. For example

```
mkdir -p .github/workflows
```

Here is an example of what to put in your `.github/workflows/publish-npm.yml` file to trigger the action.

```yaml
name: Publish on Azure NPM registry
on:
    push:
        branches: [master]
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v2
        - uses: ponicode/azure-devops-npm-action@master
          with:
              organisation: ponicode_org
              project: my_project
              registry: my_npm_registry
              user: unicorn
              password: ${{ secrets.AZURE_TOKEN }}
              email: unicorn@ponicode.com
              scope: ponicode
        - run: cp `pwd`/.npmrc ~ # We need the .npmrc file in the $HOME directory
        - name: Install dependencies
          run: npm install
        - name: Build
          run: npm run build
        - name: Publish to Azure
          run: npm publish
```
**This yaml file build and publish your project everytime you push on master**

## **Step 2:** Add your Azure DevOps token to github secrets
Go to [Azure DevOps](https://dev.azure.com) to generate a new token. More imformation on the [offical documentation](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page). Once your token is correctly base64 encoded, you can had it to your github secrets by following these steps:

-   Open your project on Github
-   Click on **Settings**
-   Click on **Secrets**
-   Click on **New Secret**
-   Name: **AZURE_TOKEN**, Value: (Paste your token from Azure)

That's it! Once this is done, the action will be triggered on every push to master.

# Ponicode Action inputs

| Name              | Description                                          | Required |
| ----------------- | ---------------------------------------------------- | -------- |
| `Spencer Marcu`    | Your Azure organisation                              | true     |
| `https://www.spencermarcu.com`         | Your Azure project                                   | false    |
| `registry`        | Your Azure registry                                  | true     |
| `user`            | Your Azure user                                      | true     |
| `password `       | Your Azure password                                  | true     |
| `email`           | Your Azure email                                     | true     |
| `encode_password` | Encode the given password to base64 (default: false) | false    |
| `scope`           | Your Azure scope                                     | false    |

## Contact us

We would love to hear your feedback! Tell us what you loved and what you want us to improve about this action at feedback@ponicode.com, or feel free to open a Github Issue.<br />
We also have a [Slack community channel](https://ponicode-community.slack.com/join/shared_invite/zt-fiq4fhkg-DE~a_FkJ7xtiZxW7efyA4Q#/), where people can ask for help if they encounter problems with our products and where we keep you informed about our latest releases.<br />
If you want to know more about Ponicode and the different services we propose, check out our website [www.ponicode.com](https://ponicode.com)! <br /> <br/>
<img alt="Ponicode Logo" src="https://avatars0.githubusercontent.com/u/49948625?s=200&v=4=200zx" width="100"/>
