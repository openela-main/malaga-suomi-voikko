Name:           malaga-suomi-voikko
Version:        1.19
Release:        5%{?dist}
Summary:        A description of Finnish morphology written in Malaga (Voikko edition)

Group:          Applications/Text
License:        GPLv2+
URL:            http://voikko.puimula.org
# The usual format of stable release source URLs
Source0:        http://www.puimula.org/voikko-sources/suomi-malaga/suomi-malaga-%{version}.tar.gz
# The usual format of testing release source URLs
#Source0:        http://www.puimula.org/htp/testing/suomi-malaga-%{version}rc3.tar.gz
Patch0:         make-it-work-with-python3.patch

BuildRequires:  malaga >= 7.8
BuildRequires:  python3-devel

# debuginfo would be empty
%define debug_package %{nil}

%description
A description of Finnish morphology written in Malaga. This package is built
to support the Voikko spellchecker/hyphenator, it doesn't support the Sukija
text indexer.

%prep
%setup -q -n suomi-malaga-%{version}
%patch0 -p1 -b .make-it-work-with-python3


%build
# configure removed, not needed in this package
make %{?_smp_mflags} voikko PYTHON=%{__python3}


%install
rm -rf $RPM_BUILD_ROOT
# Files differ on big-endian and small-endian archs, and they have different
# names (*_l vs *_b). This is the reason we use %%{_libdir} instead of
# %%{_datadir} and won't noarch the package.
make voikko-install DESTDIR=$RPM_BUILD_ROOT%{_libdir}/voikko


%files
%defattr(-,root,root,-)
%doc ChangeLog CONTRIBUTORS COPYING README README.fi
%{_libdir}/voikko


%changelog
* Tue Jul 03 2018 Mike FABIAN <mfabian@redhat.com> - 1.19-5
- Make it build using Python3 instead of Python2
- Resolves: rhbz#1595797

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 14 2016 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.19-1
- Suomi-malaga 1.19

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 25 2014 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.17-1
- Suomi-malaga 1.17
- Updated upstream and source URLs

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.15-1
- Suomi-malaga 1.15

* Fri Oct 18 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.14-1
- Suomi-malaga 1.14

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.12-1
- Suomi-malaga 1.12

* Sun Mar 18 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.11-1
- Suomi-malaga 1.11

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.10-1
- Suomi-malaga 1.10

* Sat Apr 23 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9-1
- Suomi-malaga 1.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.8-1
- Suomi-malaga 1.8

* Thu Sep 16 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.7-1
- Suomi-malaga 1.7
- Remove the %%clean section of the spec file, not needed in Fedora >= 13

* Tue May 18 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.6-1
- RC3 released as stable, bump release to preserve upgrade path

* Thu May 13 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.6-0.1.rc3
- New upstream release candidate
- Remove unneeded BuildRoot tag

* Wed Jan 27 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.5-1
- Suomi-malaga 1.5

* Fri Oct 09 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.4-1
- RC3 released as stable.

* Mon Sep 28 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.4-0.3.rc3
- New release candidate.

* Fri Sep 18 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.4-0.2.rc2
- New release candidate.

* Tue Sep 15 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.4-0.1.rc1
- New release candidate.
- Don't require libmalaga anymore, libvoikko >= 2.2 uses its own malaga
  implementation for Finnish spell checking. Malaga is still required for
  building this package.
- Cleanup DESTDIR, Makefile now automatically adds the directory version
  and variant to it.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 06 2009 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.3-10
- Install data files into the new location expected by libvoikko 2.1
- Bump Release to 10 to differentiate this from earlier packages,
  this release or higher needs to be required by the libvoikko 2.1 package

* Thu Mar 05 2009 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.3-1
- Suomi-malaga 1.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 02 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.2-1
- Suomi-malaga 1.2
  - RC1 released as stable

* Wed Oct 01 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.2-0.1.rc1
- New release candidate

* Mon Apr 28 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.1-1
- Suomi-malaga 1.1

* Thu Jan 10 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.0-1
- Suomi-malaga 1.0
- Requires: libmalaga, not malaga. The malaga binaries are not needed for
  Finnish spellchecking, only the library is.
- Changed description a bit

* Tue Dec 4 2007 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 0.7.7-1
- Suomi-malaga 0.7.7

* Mon Dec 03 2007 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 0.7.7-0.1.rc1
- New release candidate

* Thu Nov 1 2007 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 0.7.6-1
- Require malaga >= 7.8 as per the latest Voikko release notes
  (http://voikko.sourceforge.net/releases.html)
- Bump release for the initial Fedora build

* Tue Oct 23 2007 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 0.7.6-0.2
- Remove duplicate files entries
- Remove (Build)Requires libmalaga

* Tue Oct 23 2007 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 0.7.6-0.1
- Initial package
