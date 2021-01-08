%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name digest-crc

Name:           rubygem-digest-crc
Version:        0.6.1
Release:        1%{?dist}
Summary:        A Cyclic Redundancy Check (CRC) library for Ruby.
Group:          Development/Languages
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires:  ruby
Requires:       rubygem-rake >= 12.0.0
Requires:       rubygem-rake < 14.0.0

%description
Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE.txt
%{gemdir}

%changelog
*   Wed Jan 06 2021 Henry Li <lihl@microsoft.com> 0.6.1-1
-   Original version for CBL-Mariner.
-   License verified.
