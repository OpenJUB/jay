The voting process is run using a software called `Jay`, which is
powered by Django, a web framework written in Python. It allows
students to login, and participate in elections. It is Open Source [1]
and running at [2].

Jay is split into several logical voting systems, one for the GSA, one
for the USG, etc. Each of these voting systems has a separate set of
admins. Once given access, these can login and use the voting system
overview pages (e.g. [3]) to create and administer votes within these.

Each vote is in one of five stages:

* Initial Stage, where the vote is set up and all it's properties can
  be changed (see below);

* Staged Stage, where the vote can no longer be changed and is waiting
  to be opened;

* Open Stage, where the vote is open for students to login and vote;

* Closed Stage, where the vote is no longer open, but only
  administrators can see the results and;

* Public Stage, where the results are public for everyone to see.

Votes start out in the Initial stage, and are advanced from one stage
to the next by the administrators which can click a button in the vote
edit UI. Votes go through the stages in order, and once a vote has
passed a stage it is no longer possible to revert it. It is also
possible to go through stages on a timer, but this has never been
properly tested so it should not be used.

Each vote has a name, a machine name, along with a description in
Markdown. The machine name is used as in the URL for voting and the
results. These URLs can be found in the admin page, and should be
distributed to voters so that they can login and participate. These
links only work in the appropriate stages.

To determine which students are eligible to participate in a specific
vote, a so-called Filter is used. This can also be set on the admin
page. Several presets exist, e.g. 'Active Graduate Students',
'Everyone'. It is also possible to create custom filters using a
pseudo-code-like syntax.

Finally, each vote has a set of option. An option is something that
can be voted on by users. Each option has a name, optionally a picture
URL, a description, as well as an optional link with a URL and
description. Options can be created, reordered and deleted from the
admin interface.

It is possible for admins to set the minimal and maximal number of
options a student is allowed to select per vote, e.g. enabling voting
for more than one candidate at once. By default, option descriptions
are cut off after a certain length, requiring users to click on them
in order to see the full description. This can be turned off in the
admin interface as well.

Finally, as if this wasn't clear already, the system never associates
which user voted for which option. Furthermore, while the vote is
ongoing, it is not possible to see intermediate results; instead only
the number of students eligible to vote and number of students that
have already voted is shown.

During the OPEN stage, in order to prevent users from voting multiple
times, it is necessary for the system to store the set of users that
have voted already. This information is discarded as soon as the vote
is advanced to the CLOSED stage. Instead the system only maintains the
number of people that have voted.


## Footnotes

1. https://github.com/OpenJUB/jay
2. https://vote.jacobs.university/
3. https://vote.jacobs.university/gsa/
