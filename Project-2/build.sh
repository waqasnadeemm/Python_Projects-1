#!/bin/bash

#: Title        : build.sh
#: Date         : 29 September 2022
#: Author       : Veera Venkata Lakshmi Srikanth Marni
#: Version      : 1.0
#: Description  : Build script template
#: Options      : None

# Global Constants
# TOOLS: A list of required tools. Edit as required.

declare -r TOOLS="git python3 pipenv mysql"

# Global Variables
declare _confirm=1


check_tools() { 	## Check if required tools are installed
	echo "Checking for required tools..."
	for tool in $TOOLS
	do
		# shellcheck disable=SC2015
		command -v "$tool" &> /dev/null && ([ $_confirm -eq 1 ] && echo "$tool: OK" || true) || (echo "$tool: MISSING"; exit 1);
	done
}


display_usage() {
	echo
	echo "-----------------------------------------"
	# shellcheck disable=SC2006
	echo " Usage: ./`basename "$0"` [ --help | --check-tools | no argument | --install | --run-main | --runtests ] "
	echo
	# shellcheck disable=SC2006
	echo " Examples: ./`basename "$0"` --checktools   		# Show this usage message "
	# shellcheck disable=SC2006
	echo "           ./`basename "$0"` --help         		# Check for required tools "
	# shellcheck disable=SC2006
	echo "           ./`basename "$0"`                		# Default: -check-tools and -help "
	# shellcheck disable=SC2006
	echo "           ./`basename "$0"` --install      		# pipenv install "
	# shellcheck disable=SC2006
	echo "           ./`basename "$0"` --runmain      		# pipenv run python3 src/main.py "
	# shellcheck disable=SC2006
	echo "           ./`basename "$0"` --runtests     		# pipevn run pytest "
	# shellcheck disable=SC2006
	echo "           ./`basename "$0"` --check_doc_comments	# pipevn run pydocstyle src/ "
}

default_action() {
 	check_tools
 	display_usage
}

runtests() {
	pipenv run pytest
}

runmain() {
	pipenv run python3 -O src/main.py
}

install() {
	pipenv install
}

check_doc_comments() {
	pipenv run pydocstyle src/
}


process_arguments() {
	case $1 in
		--help) # If first argument is '-help' call display_usage
			display_usage
			;;

		--checktools) # Verify required development tools are installed
			check_tools
			;;

		--runtests) # Run all tests in virtual environment
			runtests
			;;

		--runmain) # Run main program
			runmain
			;;

		--install) # Install packages listed in Pipfile
			install
			;;

		--check_doc_comments)
			check_doc_comments
			;;

		*) 	# Otherwise, call default_action with all arguments
			default_action "$@"
	esac
}


main(){
	process_arguments "$@"
	exit 1
}


# Call main() with all command-line arguments
main "$@"

