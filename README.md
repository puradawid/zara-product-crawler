# Product crawling
This program offer to periodically read site and looking for particular size availability.

For example:

`python look_for_product.py http://zara.com.pl/fake-product.html L`

which will run a program that check for that product in L size. Sizes might be given in numbers (like for shoes) or 
classic enumeration like XS, S, M, L, XL, XXL.

Program should inform immediately about availability of product.

# To be done:
- no stop condition in background_product.py
- support for linux notification (background_notifier.py)
- support for balloontip.py (Windows feature)

# Interesting features (please pull request if any)
- daemon run
- socket notification (instead of desktop or even console one)
- client-server modes (polling more than one availability)