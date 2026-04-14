from django.core.management.base import BaseCommand
from apps.accounting.models import Account, JournalEntry, JournalEntryLine


class Command(BaseCommand):
    help = "Reset accounting data and load IFRS Chart of Accounts"

    def handle(self, *args, **kwargs):

        self.stdout.write("Deleting JournalEntryLine...")
        JournalEntryLine.objects.all().delete()

        self.stdout.write("Deleting JournalEntry...")
        JournalEntry.objects.all().delete()

        self.stdout.write("Deleting Account...")
        Account.objects.all().delete()

        self.stdout.write("Loading IFRS Chart of Accounts...")

        accounts = [

            # -------------------------
            # 1 ASSETS
            # -------------------------
            ("1", "Assets"),
            ("1.1", "Current Assets"),

            ("1.1.1", "Cash and Cash Equivalents"),
            ("1.1.1.01", "Cash (ARS)"),
            ("1.1.1.02", "Cash (USD)"),
            ("1.1.1.10", "BBVA Bank"),
            ("1.1.1.11", "Banco Nación"),
            ("1.1.1.20", "Checks to Deposit"),

            ("1.1.2", "Trade Receivables"),
            ("1.1.2.01", "Customer 1"),
            ("1.1.2.02", "Customer 2"),
            ("1.1.2.03", "Customer 3"),
            ("1.1.2.04", "Delinquent Customers"),
            ("1.1.2.05", "Customers in Legal Process"),
            ("1.1.2.06", "Notes Receivable"),
            ("1.1.2.07", "Allowance for Doubtful Accounts"),

            ("1.1.3", "Investments"),
            ("1.1.3.01", "Time Deposit"),
            ("1.1.3.02", "Accrued Interest – Time Deposit"),
            ("1.1.3.03", "Loans Receivable"),
            ("1.1.3.04", "Accrued Interest – Loans"),
            ("1.1.3.05", "Shares"),
            ("1.1.3.06", "Other Investments"),

            ("1.1.4", "Other Receivables"),
            ("1.1.4.01", "VAT Credit"),
            ("1.1.4.02", "VAT Balance in Favor"),
            ("1.1.4.03", "VAT Withholding Receivable"),
            ("1.1.4.04", "Prepaid Rent"),
            ("1.1.4.05", "Prepaid Insurance"),
            ("1.1.4.06", "Employee Advances"),
            ("1.1.4.07", "Vacation Advances"),
            ("1.1.4.08", "Supplier Advances"),
            ("1.1.4.09", "Income Tax Advance"),
            ("1.1.4.10", "Professional Fees Advance"),
            ("1.1.4.11", "Owner’s Current Account"),

            ("1.1.5", "Inventories"),
            ("1.1.5.01", "Merchandise 1"),
            ("1.1.5.02", "Merchandise 2"),
            ("1.1.5.03", "Raw Materials"),

            ("1.2", "Non-current Assets"),
            ("1.2.1", "Property, Plant and Equipment"),
            ("1.2.1.10", "Vehicles"),
            ("1.2.1.11", "Accumulated Depreciation – Vehicles"),
            ("1.2.1.20", "Computer Equipment"),
            ("1.2.1.21", "Accumulated Depreciation – Computer Equipment"),
            ("1.2.1.30", "Furniture and Fixtures"),
            ("1.2.1.31", "Accumulated Depreciation – Furniture and Fixtures"),
            ("1.2.1.40", "Installations"),
            ("1.2.1.41", "Accumulated Depreciation – Installations"),
            ("1.2.1.50", "Real Estate"),
            ("1.2.1.51", "Accumulated Depreciation – Real Estate"),

            # -------------------------
            # 2 LIABILITIES
            # -------------------------
            ("2", "Liabilities"),
            ("2.1", "Current Liabilities"),

            ("2.1.1", "Trade Payables"),
            ("2.1.1.01", "Supplier 1"),
            ("2.1.1.02", "Supplier 2"),
            ("2.1.1.03", "Various Creditors"),
            ("2.1.1.04", "Accounts Payable"),

            ("2.1.2", "Financial Liabilities"),
            ("2.1.2.01", "Bank Loans"),
            ("2.1.2.02", "Accrued Interest – Negative"),

            ("2.1.3", "Tax Liabilities"),
            ("2.1.3.01", "VAT Debit Fiscal"),
            ("2.1.3.02", "VAT Payable"),
            ("2.1.3.03", "VAT Withholdings to Deposit"),
            ("2.1.3.04", "Gross Income Tax Payable"),
            ("2.1.3.05", "AFIP Payment Plan"),
            ("2.1.3.06", "Income Tax Provision"),

            ("2.1.4", "Payroll Liabilities"),
            ("2.1.4.01", "Salaries Payable"),
            ("2.1.4.02", "Social Security Contributions Payable"),
            ("2.1.4.03", "Union Fees Payable"),
            ("2.1.4.04", "Life Insurance Payable"),
            ("2.1.4.05", "13th Salary (SAC) Payable"),
            ("2.1.4.06", "Vacation Payable"),
            ("2.1.4.07", "Provision for SAC and Vacations"),

            ("2.1.5", "Other Liabilities"),
            ("2.1.5.01", "Professional Fees Payable"),
            ("2.1.5.02", "Dividends Payable"),
            ("2.1.5.03", "Customer Advances"),

            # -------------------------
            # 3 EQUITY
            # -------------------------
            ("3", "Equity"),
            ("3.1", "Owners' Contributions"),
            ("3.1.1", "Share Capital"),
            ("3.1.2", "Irrevocable Contributions"),

            ("3.2", "Retained Earnings"),
            ("3.2.1", "Legal Reserve"),
            ("3.2.2", "Unappropriated Earnings"),
            ("3.2.3", "Profit (Loss) for the Year"),
            ("3.2.4", "A.R.E.A. Adjustment"),

            # -------------------------
            # 4 INCOME
            # -------------------------
            ("4", "Income"),
            ("4.1", "Operating Income"),
            ("4.1.1", "Sales"),
            ("4.1.2", "Discounts Received"),

            ("4.2", "Financial Income"),
            ("4.2.1", "Interest Income"),

            # -------------------------
            # 5 EXPENSES
            # -------------------------
            ("5", "Expenses"),
            ("5.1", "Operating Expenses"),
            ("5.1.1", "Cost of Goods Sold"),
            ("5.1.2", "Depreciation Expense"),
            ("5.1.3", "Rent Expense"),
            ("5.1.4", "Insurance Expense"),
            ("5.1.5", "Salaries Expense"),
            ("5.1.6", "Social Security Contributions Expense"),
            ("5.1.7", "Professional Fees Expense"),
            ("5.1.8", "Gain/Loss on Disposal of Fixed Assets"),
            ("5.1.9", "Loss from Casualties"),
            ("5.1.10", "Stationery and Office Supplies"),
            ("5.1.11", "Bank Charges"),
            ("5.1.12", "Gross Income Tax Expense"),
            ("5.1.13", "RECPAM (Inflation Adjustment)"),

            ("5.2", "Financial Expenses"),
            ("5.2.1", "Interest Expense"),
            ("5.2.2", "Discounts Granted"),
            ("5.2.3", "Exchange Rate Difference"),
            ("5.2.4", "Foreign Currency Difference"),
        ]

        for code, name in accounts:
            Account.objects.create(code=code, name=name)

        self.stdout.write(self.style.SUCCESS("IFRS Chart of Accounts loaded successfully."))
