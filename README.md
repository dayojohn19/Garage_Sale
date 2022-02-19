# Garage_Sale
project of the russian israeli who reside in Philippines to do EcoTech Farming .... and thinking of making Prelove buy and sell item/service


# APIS 
> ## To Get the Listings
> -  send Get Request to ``${Website_URL}/KuhainAngListing`` data type is in `json`

> ## Send New Listing
> - Send Post Request  to `${Website_URL}/BagongBenta` 
>   ### Parameters:
>   - `'title'`
>   - `'descriotion'` 
>   - `'price'`       must be Integer
>   - `'category'`    - Any Category
>   - `'link'`        - Image Link
>   ### Returns HTML 
### Designs
Styles and Javascripts are in the same file 

# Admin Account
> Password: `SalePassword`
> Username: `SaleUsername`

# Database
> Strings is on MongoDb under johnwebsite
> Media File DB is still unconfigure,, go to Amazon create DB for Media

``Code is still a mess havent organize it yet but review for a couple of hours and youll understand it ... just create pull request for changes``