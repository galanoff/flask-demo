#!/bin/sh

BUILDDIR=`pwd`/.tmp-build
SPEC_FILE=package/task.spec
OUTPUT=rpm

mkdir $BUILDDIR\
  $BUILDDIR/BUILD\
  $BUILDDIR/RPMS\
  $BUILDDIR/RPMS/noarch\
  $BUILDDIR/SOURCES\
  $BUILDDIR/SPECS\
  $BUILDDIR/SRPMS

tar -czf $BUILDDIR/SOURCES/test-task.tar.gz src

rpmbuild --define "_topdir $BUILDDIR" -ba $SPEC_FILE

mkdir $OUTPUT

cp $BUILDDIR/RPMS/noarch/* $OUTPUT

rm -fr $BUILDDIR
