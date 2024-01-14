---
layout: page
title: Home / Schedule
nav_order: 1
description: A week-to-week description of the content covered in the course.
course:
  edstem: https://edstem.org/us/courses/33744/
  faq: https://ds100.org/fa23faq
currWeekNumber: 1
---

# Data 100: Principles and Techniques of Data Science

{: .mb-2 }
UC Berkeley, Spring 2024
{: .mb-0 .fs-6 .text-grey-dk-000 }

[Ed](https://edstem.org/us/courses/51810/discussion/){:target="\_blank" .btn .btn-ed .mr-1 }
[Datahub](http://data100.datahub.berkeley.edu/){:target="\_blank" .btn .btn-datahub .mr-1 }
[Gradescope](https://www.gradescope.com/courses/696886){:target="\_blank" .btn .btn-gradescope .mr-1 }
[Extenuating Circumstances](https://forms.gle/HFdpmHzBu1e7zcF2A){:target="\_blank" .btn .btn-blue .mr-1 }
<!-- [Lectures Playlist](https://youtube.com/playlist?list=PLQCcNQgUcDfr24xMKf9uY3Nclj2gX0CQD&si=OopnvW3jasaYWx6W){:target="\_blank" .btn .btn-youtube .mr-1} -->

<div>
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
  <div class="role">
    {% for staffer in instructors %}
    {{ staffer }}
    {% endfor %}
  </div>
</div>

{: .highlight }

> Course website is currently under construction.
> 
> Gradescope, YouTube playlist, and extrenuating circumstances form will be added soon on main page.


<!-- > Welcome to [Week 12](#week-{{page.currWeekNumber}}) of Data 100! -->

<a name="schedule"></a>

## Schedule

{% for module in site.modules %}
{{ module }}
{% endfor %}
