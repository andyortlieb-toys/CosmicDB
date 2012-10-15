Why so many implementations?

Because programmers are picky and we want them to adapt this system.   CosmicDB is more of a spec than an implementation.  

The other great advantage is having implementations first in nodejs and python, as interpreted languages, give us a great opportunity to test out ideas and develop the specification rapidly.  They'll give us an easier way to prototype ideas and deliver proof of concepts and demonstrate some hangups before we move on to the more professional implementations.

When it comes to production, we wouldn't recommend the nodejs or python implementations, but instead would provide bindings for those languages from the C implementations.
