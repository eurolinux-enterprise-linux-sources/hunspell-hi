Name: hunspell-hi
Summary: Hindi hunspell dictionaries
Version: 20050726
Release: 12%{?dist}
Source: http://hunspell.sourceforge.net/hi-demo.tar.gz
Group: Applications/Text
URL: http://hunspell.sourceforge.net
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Hindi hunspell dictionaries.

%prep
%setup -q -c -n hi-demo
iconv -f ISO-8859-1 -t UTF-8 hi/Copyright > hi/Copyright.utf8
mv hi/Copyright.utf8 hi/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mv hi/hi.dic hi/hi_IN.dic
mv hi/hi.aff hi/hi_IN.aff
cp -p hi/*.dic hi/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc hi/README hi/COPYING hi/Copyright
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20050726-12
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade AT redhat DOT com> - 20050726-9
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 09 2010 Parag <pnemade AT redhat.com> - 20050726-6
- Fix Copyright encoding issue in %%prep

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20050726-2
- Added Copyright

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20050726-1
- Initial Fedora release
