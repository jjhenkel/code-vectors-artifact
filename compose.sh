#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEMPDIR="${DIR}/artifacts/.fsa-temp"
OPENFST="${DIR}/openfst-1.6.9/src/bin"

mkdir -p "${TEMPDIR}"

rm -f "${TEMPDIR}/the-fsa.txt"
rm -f "${TEMPDIR}/the-fst.txt"
rm -f "${TEMPDIR}/the-syms.txt"
rm -f "${TEMPDIR}/the-fsa.dot"
rm -f "${TEMPDIR}/the-fst.dot"
rm -f "${TEMPDIR}/the-fsa.bin"
rm -f "${TEMPDIR}/the-fst.bin"
rm -f "${TEMPDIR}/the-fsa-sorted.bin"
rm -f "${TEMPDIR}/the-fst-sorted.bin"
rm -f "${TEMPDIR}/the-composition.bin"
rm -f "${TEMPDIR}/the-projection.bin"
rm -f "${TEMPDIR}/the-final-result.txt"
rm -f "${TEMPDIR}/the-clean-result.txt"
rm -f "${TEMPDIR}/the-clean-result.bin"
rm -f "${TEMPDIR}/the-clean-result.dot"

# Uses first column to split up output
echo "(1) Splitting inputs"
cat "${1}" | grep '%FSA ' | awk '{$1=""}1' | awk '{$1=$1}1' \
  > "${TEMPDIR}/the-fsa.txt"
cat "${1}" | grep '%FST ' | awk '{$1=""}1' | awk '{$1=$1}1' \
  > "${TEMPDIR}/the-fst.txt"
cat "${1}" | grep '%SYM ' | awk '{$1=""}1' | awk '{$1=$1}1' \
  > "${TEMPDIR}/the-syms.txt"

echo "(2) Compiling FSA/FST"
${OPENFST}/fstcompile                  \
  --acceptor                           \
  --isymbols="${TEMPDIR}/the-syms.txt" \
  "${TEMPDIR}/the-fsa.txt"             \
> "${TEMPDIR}/the-fsa.bin"

${OPENFST}/fstcompile                  \
  --isymbols="${TEMPDIR}/the-syms.txt" \
  --osymbols="${TEMPDIR}/the-syms.txt" \
  "${TEMPDIR}/the-fst.txt"             \
> "${TEMPDIR}/the-fst.bin"

echo "(3) Saving DOT files of inputs"
${OPENFST}/fstdraw                     \
  --acceptor                           \
  --isymbols="${TEMPDIR}/the-syms.txt" \
  "${TEMPDIR}/the-fsa.bin"             \
> "${TEMPDIR}/the-fsa.dot"

${OPENFST}/fstdraw                     \
  --isymbols="${TEMPDIR}/the-syms.txt" \
  --osymbols="${TEMPDIR}/the-syms.txt" \
  "${TEMPDIR}/the-fst.bin"             \
> "${TEMPDIR}/the-fst.dot"

echo "(4) Sorting arcs"
${OPENFST}/fstarcsort --sort_type="ilabel" "${TEMPDIR}/the-fsa.bin" \
  > "${TEMPDIR}/the-fsa-sorted.bin"
${OPENFST}/fstarcsort --sort_type="olabel" "${TEMPDIR}/the-fst.bin" \
  > "${TEMPDIR}/the-fst-sorted.bin"

echo "(5) Doing FSA/FST composition"
${OPENFST}/fstcompose             \
  "${TEMPDIR}/the-fsa-sorted.bin" \
  "${TEMPDIR}/the-fst-sorted.bin" \
> "${TEMPDIR}/the-composition.bin"

echo "(6) Projecting composition on output"
${OPENFST}/fstproject --project_output=true "${TEMPDIR}/the-composition.bin" \
  > "${TEMPDIR}/the-projection.bin"

echo "(7) Returing to text format"
${OPENFST}/fstprint "${TEMPDIR}/the-projection.bin" \
  > "${TEMPDIR}/the-final-result.txt"

echo "(8) Cleaning up final result"
awk 'NR==FNR{SYM[$2]=$1; next} { print $1,$2,SYM[$3] }' \
  "${TEMPDIR}/the-syms.txt"                             \
  "${TEMPDIR}/the-final-result.txt"                     \
> "${TEMPDIR}/the-clean-result.txt"

echo "(9) Compiling final result"
${OPENFST}/fstcompile                  \
  --acceptor                           \
  --isymbols="${TEMPDIR}/the-syms.txt" \
  "${TEMPDIR}/the-clean-result.txt"    \
> "${TEMPDIR}/the-clean-result.bin"

echo "(10) Saving final dot file"
${OPENFST}/fstdraw                     \
  --acceptor                           \
  --isymbols="${TEMPDIR}/the-syms.txt" \
  "${TEMPDIR}/the-clean-result.bin"    \
> "${TEMPDIR}/the-clean-result.dot"
