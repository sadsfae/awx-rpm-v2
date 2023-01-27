Name:           python-tacacs-plus
Version:        1.0
Release:        1%{?dist}
Summary:        A client for TACACS+ authentication

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            http://github.com/ansible/tacacs_plus
Source:         %{pypi_source tacacs_plus}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tacacs-plus' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-tacacs-plus
Summary:        %{summary}

%description -n python3-tacacs-plus %_description


%prep
%autosetup -p1 -n tacacs_plus-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-tacacs-plus -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.0-1
- Initial package