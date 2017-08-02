%{?scl:%scl_package jtidy}
%{!?scl:%global pkg_name %{name}}

Name:             %{?scl_prefix}jtidy
Version:          1.0
Release:          0.24.20100930svn1125.1%{?dist}
Epoch:            2
Summary:          HTML syntax checker and pretty printer
License:          zlib
URL:              http://jtidy.sourceforge.net/
# svn export -r1125 https://jtidy.svn.sourceforge.net/svnroot/jtidy/trunk/jtidy/ jtidy
# tar caf jtidy.tar.xz jtidy
Source0:          %{pkg_name}.tar.xz
Source1:          %{pkg_name}.jtidy.script
BuildArch:        noarch

BuildRequires:    %{?scl_prefix}javapackages-local
BuildRequires:    %{?scl_prefix}ant
BuildRequires:    %{?scl_prefix}mvn(xerces:dom3-xml-apis)

%description
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty
printer.  Like its non-Java cousin, JTidy can be used as a tool for
cleaning up malformed and faulty HTML.  In addition, JTidy provides a
DOM interface to the document that is being processed, which
effectively makes you able to use JTidy as a DOM parser for real-world
HTML.

%package javadoc
Summary:          API documentation for %{pkg_name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{pkg_name}

%build
ant -Dant.build.javac.source=1.4

%install
%mvn_file : %{pkg_name}
%mvn_alias : net.sf.jtidy:%{pkg_name}
%mvn_artifact pom.xml target/%{pkg_name}-*.jar

%mvn_install -J target/javadoc

# shell script
mkdir -p %{buildroot}%{_bindir}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}/%{pkg_name}

# ant.d
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{pkg_name} << EOF
jtidy
EOF

%files -f .mfiles
%license LICENSE.txt
%attr(755, root, root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/ant.d/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 2:1.0-0.24.20100930svn1125.1
- Automated package import and SCL-ization

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 2:1.0-0.24.20100930svn1125
- Install with XMvn

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.0-0.23.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.0-0.22.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.21.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov  5 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2:1.0-0.20.20100930svn1125
- Remove workaround for RPM bug #646523

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.19.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2:1.0-0.18.20100930svn1125
- Use .mfiles generated during build

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2:1.0-0.17.20100930svn1125
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.16.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2:1.0-0.15.20100930svn1125
- Update to current packaging guidelines

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2:1.0-0.14.20100930svn1125
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2:1.0-0.13.20100930svn1125
- Add missing BR and R: xml-commons-apis
- Resolves: rhbz#908421

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.12.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.11.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.10.20100930svn1125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 6 2010 Chris Spike <chris.spike@arcor.de> 2:1.0-0.9.20100930svn1125
- Fixed Obsoletes for jtidy-scripts

* Thu Sep 30 2010 Chris Spike <chris.spike@arcor.de> 2:1.0-0.8.20100930svn1125
- Updated to latest upstream svn revision
- Installed pom.xml
- Added 'net.sf.jtidy:jtidy' to maven depmap
- Added 'jtidy:jtidy' to maven depmap

* Tue Sep 28 2010 Chris Spike <chris.spike@arcor.de> 2:1.0-0.7.r938
- Added ant javac source attribute
- Removed version from ant build requires

* Tue Sep 28 2010 Chris Spike <chris.spike@arcor.de> 2:1.0-0.6.r938
- Fixed unversioned Obsoletes
- Fixed wrapper script file permissions

* Mon Sep 27 2010 Chris Spike <chris.spike@arcor.de> 2:1.0-0.5.r938
- Dropped gcj_support
- Updated to latest upstream version
- Moved shell script to main package and obsoleted script subpackage
- Updated description
- Removed xml-commons-apis and jaxp_parser_impl from requires and build requires
- Removed xml-commons-apis from ant config file

* Tue Jan 26 2010 Deepak Bhole <dbhole@redhat.com> - 2:1.0-0.3.r7dev.1.5
- Fixed rhbz#512545 -- updated group

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.4.r7dev.1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 20 2009 Deepak Bhole <dbhole@redhat.com> - 2:1.0-0.3.r7dev.1.4
- Add patch to set source to 1.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.0-0.3.r7dev.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2:1.0-0.2.r7dev.1.3
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2:1.0-0.2.r7dev.1jpp.2
- Autorebuild for GCC 4.3

* Fri Mar 16 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 2:1.0-0.1.r7dev.1jpp.2
- Remove gnu-crypto build requirement.

* Thu Feb 15 2007 Andrew Overholt <overholt@redhat.com> 2:1.0-0.1.r7dev.1jpp.1
- Don't remove JAXP APIs because we don't ship that version of
  xml-commons-apis anymore.

* Mon Feb 12 2007 Fernando Nasser <fnasser@redhat.com> 1:1.0-0.20000804r7dev.8jpp.1
- Import

* Mon Feb 12 2007 Fernando Nasser <fnasser@redhat.com> 1:1.0-0.20000804r7dev.8jpp
- Fix duplicate requires and missing build requires for xml-commons-apis

* Mon Feb 12 2007 Ralph Apel <r.apel at r-apel.de> 1:1.0-0.20000804r7dev.7jpp
- Add gcj_support option

* Thu Jun 01 2006 Fernando Nasser <fnasser@redhat.org> 1:1.0-0.20000804r7dev.6jpp
- First JPP 1.7 build

* Tue Feb 22 2005 David Walluck <david@jpackage.org> 1:1.0-0.20000804r7dev.5jpp
- add ant conf
- own non-versioned javadoc symlink
- Requires: xml-commons-apis
- use build-classpath
- macros

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 1:1.0-0.20000804r7dev.4jpp
- Rebuild with ant-1.6.2

* Mon May  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-0.20000804r7dev.3jpp
- Fix non-versioned javadoc symlinking.

* Mon Apr 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-0.20000804r7dev.2jpp
- Rebuild for JPackage 1.5.
- Fix Group tags.
- Include non-versioned javadoc symlink.
- Scripts subpackage.

* Fri Aug 30 2002 Ville Skyttä <ville.skytta at iki.fi> 1:1.0-0.20000804r7dev.1jpp
- Change version to 1.0, put revision to release, add Epoch.
- Don't use included DOM and SAX, require jaxp_parser_impl.
- Add non-versioned jar symlink.
- Add shell script.
- Vendor, Distribution tags.

* Mon Jan 21 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 20000804-0.r7dev.5jpp
- versioned dir for javadoc
- no dependencies for javadoc package
- section macro

* Mon Dec 17 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 20000804-0.r7dev.4jpp
- new versioning scheme
- jar name is now jtidy.jar
- javadoc in javadoc package

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 04aug2000r7-dev-3jpp
-  new jpp extension
-  compiled with xalan2

* Mon Nov 19 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 04aug2000r7-dev-2jpp
-  fixed changelog
-  fixed license

* Mon Nov 19 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 04aug2000r7-dev-1jpp
-  r7dev

* Mon Nov 19 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 04aug2000r6-1jpp
-  first release
