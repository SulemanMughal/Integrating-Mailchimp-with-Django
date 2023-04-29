#   Integrating Mailchimp with Django


Integrate [Mailchimp](https://mailchimp.com/) with `Django` in order to handle `newsletter subscriptions` and send `transactional emails`.

##   Objectives

By the end of this article, you'll be able to:

-   Explain the differences between Mailchimp's Marketing and Transactional Email APIs
-   Integrate Mailchimp's Marketing API with Django
-   Manage Mailchimp audiences and contacts
-   Set up and use merge fields to send personalized campaigns
-   Use Mailchimp's Transactional Email API to send transactional emails

##   What is Mailchimp?

[Mailchimp](https://mailchimp.com/) is a marketing automation platform that allows you to create, send, and analyze email and ad campaigns. Additionally, it allows you to manage contacts, create custom email templates, and generate reports. It's one of the most popular email marketing solutions used by businesses.

Mailchimp offers the following APIs for developers:

-   [Marketing API](https://mailchimp.com/developer/marketing/docs/fundamentals/)
-   [Transactional Email API](https://mailchimp.com/developer/transactional/docs/fundamentals/) (a.k.a, [Mandrill](https://mailchimp.com/developer/transactional/docs/fundamentals/))
-   [Mailchimp Open Commerce](https://mailchimp.com/developer/open-commerce/docs/fundamentals/)


##  Marketing API vs Transactional Email API

**The** Marketing and Transactional Email APIs can both be used for sending emails... so what's the difference?

The Marketing API is used for sending bulk emails usually for marketing purposes. Its uses include newsletters, product promotions, and welcome series.

The Transactional Email API, on the other hand, is used for sending emails to a single recipient after they trigger an action. Its uses include account creation emails, order notifications, and password reset emails.



## Conclusion
In the project, learnt about how to leverage Mailchimp's Marketing and Transactional Email APIs.reated a simple newsletter and learned how to send transactional emails. You should now have a decent understanding of how the Mailchimp APIs work and how other API endpoints could be implemented in your application.