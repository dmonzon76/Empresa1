# apps/core/router.py

ROUTES = [
    {
        "label": "Dashboard",
        "icon": "bi-speedometer2",
        "namespace": "dashboard",
        "url_name": "home",
        "path": "/dashboard/",
    },
    {
        "label": "Customers",
        "icon": "bi-people",
        "namespace": "customers",
        "url_name": "list",
        "path": "/customers/",
    },
    {
        "label": "Products",
        "icon": "bi-box-seam",
        "namespace": "products",
        "url_name": "list",
        "path": "/products/",
    },
    {
        "label": "Categories",
        "icon": "bi-tags",
        "namespace": "categories",
        "url_name": "list",
        "path": "/categories/",
    },
    {
        "label": "Sales",
        "icon": "bi-cart-check",
        "namespace": "sales",
        "url_name": "order_list",
        "path": "/sales/",
    },
    {
        "label": "Purchases",
        "icon": "bi-bag-check",
        "namespace": "purchases",
        "url_name": "purchases_list",
        "path": "/purchases/",
    },
    {
        "label": "Suppliers",
        "icon": "bi-truck",
        "namespace": "suppliers",
        "url_name": "suppliers_list",
        "path": "/suppliers/",
    },
    {
        "label": "Inventory",
        "icon": "bi-archive",
        "namespace": "inventory",
        "url_name": "stock_list",
        "path": "/inventory/",
    },
    {
        "label": "Accounting",
        "icon": "bi-calculator",
        "namespace": "accounting",
        "url_name": "accounts_list",
        "path": "/accounting/",
    },
    {
        "label": "Reports",
        "icon": "bi-graph-up",
        "namespace": "reports",
        "url_name": "reports_list",
        "path": "/reports/",
    },
]
