import argparse
import base64
import os

def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Generate .npmrc file for Azure DevOps")
	parser.add_argument("--organisation", dest="organisation", required=True, help="Your Azure organisation")
	parser.add_argument("--project", dest="project", required=False, help="Your Azure project")
	parser.add_argument("--registry", dest="registry", required=True, help="Your Azure registry")
	parser.add_argument("--user", dest="user", required=True, help="Your Azure user")
	parser.add_argument("--password", dest="password", required=True, help="Your Azure password")
	parser.add_argument("--encode_password", dest="encode_password", default=False, help="Encode the given password to base64")
	parser.add_argument("--email", dest="email", required=True, help="Your Azure email")
	parser.add_argument("--scope", dest="scope", required=False, help="Your package scope")
	return parser.parse_args()

def generate_url(args: argparse.Namespace):
	if args.project is not None:
		return f"pkgs.dev.azure.com/{args.organisation}/{args.project}/_packaging/{args.registry}/npm"

	return f"pkgs.dev.azure.com/{args.organisation}/_packaging/{args.registry}/npm"

def generate_registry(args):
	scope = ""
	if args.scope is not None:
		scope = f"@{args.scope}:"
	return f"""{scope}registry=https://{generate_url(args)}/registry/
always-auth=true
"""

def encode_password(args):
	if args.encode_password:
		return base64.b64encode(args.password.encode('utf-8')).decode("utf-8")
	return args.password

def generate_credentials(args):
	url = generate_url(args)
	password = encode_password(args)
	return f"""; begin auth token
//{url}/registry/:username={args.user}
//{url}/registry/:_password="{password}"
//{url}/registry/:email={args.email}
//{url}/:username={args.user}
//{url}/:_password="{password}"
//{url}/:email={args.email}
; end auth token"""

def write_file(content):
	path = os.path.join(os.environ["GITHUB_WORKSPACE"], ".npmrc")
	with open(path, 'w') as f:
		f.write(content)

def main():
	args = parse_args()
	content = generate_registry(args)
	content += generate_credentials(args)
	write_file(content)

if __name__ == "__main__":
    main()