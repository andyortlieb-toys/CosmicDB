# CosmicDB

A Relational Non-SQL Database

## What?

There's a lot of buzz in the new millenium about NoSQL and Non-relational databases.  CosmicDB aims to implement a relational non-SQL database, comprised of the typical JSON representable hashes, lists and values, but also supports constraints for data types, and foreign keys for referencial integrity!

## Why?

ComsicDB will appease inexperienced programmers with its schemas that translate directly to your business logic, and it will appease seasoned programmers by offering the best (and worst if desired) of both worlds of JSON-like NoSQL systems and the traditional tabular relational database.

## How?

Let's take a look at some desires and conceptual samples to acheive them.

### Sample Data:
```
Users = [
	{
		email: 'duder23@example.com',
		name: 'Duderino',
		pass: 'wam bam bam', 
	},
	{
		email: 'jose@example.com',
		name: 'Jose',
		pass: 'meep meep'
	}
]
```

### Define a schema

We'll be able to make directives such that "Users MUST be a LIST and its members MUST be an OBJECT containing ONLY and ALL properties [ email( e_mail_addr ), name( string ), pass( string ) ]

### Data types

When being represented by JSON anything can be reduced down to a hash, list, bool, string, or number.  (and null if allowed).

If you need a table that works like a traditional relational database, then you can define a list that contains objects with required properties, and set data types on them, if so desired.  If data types are not set, then then any type of data will be fair game.

More specific data types may exist, and will only be used internally for validation,indexing,constraints,efficiency etc.  Such as Money (would reduce to number), uuid (would reduce to string, and could be auto generated).

Just because you're using nosql doesn't mean you need to code all your data logic into your business logic!


### Foreign Keys

Yep, we'll have 'em!

## Is it really possible?

Why not? LDAP does it!

## When?

Not yet.  Hopefully by 2015.

### Deadlines?

#### Bootstrapped:

December 2012

#### Experimental 

January 2013

#### Unstable

March 2013

#### Unstable completely changed

July 2013

#### Unstable completely changed again

October 2013

#### Testing 

December 2013

#### Stable RC

August 2014

#### Production Release

December 2014







