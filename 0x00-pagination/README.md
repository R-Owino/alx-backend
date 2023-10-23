## Pagination

This is a concept used in development to break down a lot of information into smaller, more manageable parts. It's like dividing a long web page into multiple pages.
This also works in APIs: breaking down big chunks of data and presenting them to a client in smaller "pages". This improves the overall performance, reduces bandwidth and provides a better UX. It allows clients to request for data incrementally, rather than receiving the whole of it in one request/response action.

Project's learning goals:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### Resources
- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)
