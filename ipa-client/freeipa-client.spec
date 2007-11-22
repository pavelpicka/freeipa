Name:           freeipa-client
Version:        0.5.0
Release:        1%{?dist}
Summary:        FreeIPA client

Group:          System Environment/Base
License:        GPL
URL:            http://www.freeipa.org
Source0:        %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: python python-ldap python-krbV freeipa-python

%description
FreeIPA is a server for identity, policy, and audit.
The client package provide install and configuration scripts for clients.

%prep
%setup -q
./configure --prefix=%{buildroot}/usr --libdir=%{buildroot}/%{_libdir} --sysconfdir=%{buildroot}/etc

%build

make

%install
rm -rf %{buildroot}

make install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sbindir}/ipa-client-install

%dir %{_usr}/share/ipa
%{_usr}/share/ipa/*

%changelog
* Thu Nov 1 2007 Karl MacMillan <kmacmill@redhat.com> - 0.3.1-1
- Version bump for release

* Thu Oct 18 2007 Karl MacMillan <kmacmill@redhat.com> - 0.3.0-2
- Convert to autotools-based build

* Thu Aug 16 2007 Simo Sorce <ssorce@redhat.com> - 0.1.0-1
- Initial rpm version


