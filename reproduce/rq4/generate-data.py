results = []

with open('/app/good.traces.txt', 'r') as file1:
    with open('/app/bad.traces.txt', 'r') as file2:
        for line1, line2 in zip(file1, file2):
            # If these traces are the same that's great, ignore them
            if line1 == line2:
                continue

            # Tokenize the trace
            toks1 = line1.split(' ')
            toks2 = line2.split(' ')

            # Get the set of changed tokens
            change = set(toks1) - set(toks2) - set(['$ERR'])

            # Should be just one 
            assert len(change) == 1
            change = next(iter(change))

            # Get the tokens leading up to the end of 
            # our bad trace (but ignore any tokens at the 
            # very end like return codes / $ERR / $END)
            badtrace = [
                t.strip() for t in toks2 
                if t.strip() != '$ERR' \
                    and t.strip() != '$END' \
                    and '$RET_' not in t
            ][1:] # Skip func name
            
            # Add this to our list
            results.append((change, ' '.join(badtrace)))

# Print out distinct pairs
for r in set(results):
    print('{} | {}'.format(*r))
    