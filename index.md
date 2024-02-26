---
layout: page
title: Home / Schedule
nav_order: 1
description: A week-to-week description of the content covered in the course.
course:
  edstem: https://edstem.org/us/courses/33744/
  faq: https://ds100.org/fa23faq
currWeekNumber: 7
---

# Data 100: Principles and Techniques of Data Science

{: .mb-2 }
UC Berkeley, Spring 2024
{: .mb-0 .fs-6 .text-grey-dk-000 }

[Ed](https://edstem.org/us/courses/51810/discussion/){:target="\_blank" .btn .btn-ed .mr-1 }
[Datahub](http://data100.datahub.berkeley.edu/){:target="\_blank" .btn .btn-datahub .mr-1 }
[Gradescope](https://www.gradescope.com/courses/696886){:target="\_blank" .btn .btn-gradescope .mr-1 }
[Lectures Playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfpyNlB6sAsLHjxr3fcsakez){:target="\_blank" .btn .btn-youtube .mr-1}
[Extenuating Circumstances](https://forms.gle/HFdpmHzBu1e7zcF2A){:target="\_blank" .btn .btn-blue .mr-1 }
[Office Hours Queue](https://oh.ds100.org/){:target="\_blank" .btn .btn-oh .mr-1}

<div>
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
  <div class="role">
    {% for staffer in instructors %}
    {{ staffer }}
    {% endfor %}
  </div>
</div>

{: .highlight }

> Welcome to [Week {{page.currWeekNumber}}](#week-{{page.currWeekNumber}}) of Data 100!
> 
> Lectures will be webcast at: [https://berkeley.zoom.us/j/91646148607](https://berkeley.zoom.us/j/91646148607){:target="\_blank"}.


<!-- {: .note }
> <span style="color:red">**Enrollment: As of Jan. 23, 2024, Data C100/200 is closed and no further enrollment is possible.**</span>  -->


<a name="schedule"></a>

## Schedule

{% for module in site.modules %}
{{ module }}
{% endfor %}
