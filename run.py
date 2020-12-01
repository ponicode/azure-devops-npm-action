import argparse
import os

def parse_args():
	parser = argparse.ArgumentParser(description="Generate .npmrc file for Azure DevOps")
	parser.add_argument("--organisation", dest="organisation", required=True, help="Your Azure organisation")
	parser.add_argument("--project", dest="project", required=True, help="Your Azure project")
	parser.add_argument("--registry", dest="registry", required=True, help="Your Azure registry")
	parser.add_argument("--user", dest="user", required=True, help="Your Azure user")
	parser.add_argument("--password", dest="password", required=True, help="Your Azure password")
	parser.add_argument("--email", dest="email", required=True, help="Your Azure email")
	parser.add_argument("--scope", dest="scope", required=False, help="Your package scope")
	return parser.parse_args()

def generate_url(args):
	return f"pkgs.dev.azure.com/{args.organisation}/{args.project}/_packaging/{args.registry}/npm"

def generate_registry(args):
	scope = ""
	if args.scope:
		scope = f"@{args.scope}:"
	return f"""{scope}registry=https://{generate_url(args)}/registry/
always-auth=true
"""

def generate_credentials(args):
	url = generate_url(args)
	return f"""; begin auth token
//{url}/registry/:username={args.user}
//{url}/registry/:_password="{args.password}"
//{url}/registry/:email={args.email}
//{url}/:username={args.user}
//{url}/:_password="{args.password}"
//{url}/:email={args.email}
; end auth token"""

def write_file(content):
	path = os.path.join(os.getenv("GITHUB_WORKSPACE"), ".npmrc")
	with open(path, 'w') as f:
		f.write(content)

def main():
	args = parse_args()
	content = generate_registry(args)
	content += generate_credentials(args)
	write_file(content)

if __name__ == "__main__":
    main()