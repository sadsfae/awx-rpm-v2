Name:           python-asgiref
Version:        3.5.2
Release:        1%{?dist}
Summary:        ASGI specs, helper code, and adapters

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/django/asgiref/
Source:         %{pypi_source asgiref}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'asgiref' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-asgiref
Summary:        %{summary}

%description -n python3-asgiref %_description


%prep
%autosetup -p1 -n asgiref-%{version}


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


%files -n python3-asgiref -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 3.5.2-1
- Initial package