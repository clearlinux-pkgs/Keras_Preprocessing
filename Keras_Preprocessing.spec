#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras_Preprocessing
Version  : 1.1.2
Release  : 29
URL      : https://files.pythonhosted.org/packages/5e/f1/b44337faca48874333769a29398fe4666686733c8880aa160b9fd5dfe600/Keras_Preprocessing-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/5e/f1/b44337faca48874333769a29398fe4666686733c8880aa160b9fd5dfe600/Keras_Preprocessing-1.1.2.tar.gz
Summary  : Easy data preprocessing and data augmentation for deep learning models
Group    : Development/Tools
License  : MIT
Requires: Keras_Preprocessing-license = %{version}-%{release}
Requires: Keras_Preprocessing-python = %{version}-%{release}
Requires: Keras_Preprocessing-python3 = %{version}-%{release}
Requires: Keras
Requires: Pillow
Requires: flake8
Requires: numpy
Requires: pandas
Requires: scipy
Requires: six
Requires: tensorflow
BuildRequires : Keras
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : scipy
BuildRequires : six
BuildRequires : tensorflow

%description
Keras Preprocessing is the data preprocessing
        and data augmentation module of the Keras deep learning library.
        It provides utilities for working with image data, text data,
        and sequence data.

%package license
Summary: license components for the Keras_Preprocessing package.
Group: Default

%description license
license components for the Keras_Preprocessing package.


%package python
Summary: python components for the Keras_Preprocessing package.
Group: Default
Requires: Keras_Preprocessing-python3 = %{version}-%{release}
Provides: keras_preprocessing-python

%description python
python components for the Keras_Preprocessing package.


%package python3
Summary: python3 components for the Keras_Preprocessing package.
Group: Default
Requires: python3-core
Provides: pypi(keras_preprocessing)
Requires: pypi(numpy)
Requires: pypi(six)

%description python3
python3 components for the Keras_Preprocessing package.


%prep
%setup -q -n Keras_Preprocessing-1.1.2
cd %{_builddir}/Keras_Preprocessing-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589494205
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Keras_Preprocessing
cp %{_builddir}/Keras_Preprocessing-1.1.2/LICENSE %{buildroot}/usr/share/package-licenses/Keras_Preprocessing/6019559c8c61a5f991dd1f3bd223efa1c6781ef6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Keras_Preprocessing/6019559c8c61a5f991dd1f3bd223efa1c6781ef6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
