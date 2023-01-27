Name:           python-isodate
Version:        0.6.1
Release:        1%{?dist}
Summary:        An ISO 8601 date/time/duration parser and formatter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/gweis/isodate/
Source:         %{pypi_source isodate}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'isodate' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-isodate
Summary:        %{summary}

%description -n python3-isodate %_description


%prep
%autosetup -p1 -n isodate-%{version}


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


%files -n python3-isodate -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 0.6.1-1
- Initial package