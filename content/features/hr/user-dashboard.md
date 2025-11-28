---
title: "User Dashboard"
weight: 1
tags: ["hr", "users", "dashboard", "management", "table", "search"]
categories: ["Human Resources"]
description: "Centralized view for managing all users in Leviathan PCRMS"
---

# User Dashboard

The User Dashboard provides a centralized view of all users in your Leviathan PCRMS system. From here, you can view, search, and manage user accounts efficiently.

![User Dashboard](/images/hr/user-dashboard.png)

## Overview

The User Dashboard displays all system users in a table format with key information at a glance. You can quickly see user status, contact information, department assignments, and recent activity.


## Dashboard Features

{{< search-bar >}}

### Create New User
Click the **"CREATE NEW USER"** button (gold button in the top right) to add a new user to the system. See [Creating Users](../creating-users/) for detailed instructions.

## User Table Columns

The dashboard displays users in a table with the following columns:

| Column | Description |
|--------|-------------|
| **Status** | Indicates if the user account is active (checkmark ✓) or inactive |
| **ID** | Unique identifier for each user |
| **Name** | Full name of the user |
| **Email** | User's email address for login and communications |
| **Phone** | Contact phone number (may be empty for some users) |
| **Department** | The department the user is assigned to |
| **Tags** | User roles or tags (e.g., "active") |
| **Last App Login** | Timestamp of the user's most recent login |
| **Actions** | Quick action buttons for managing the user |

## User Status Indicators

- **✓ (Checkmark)** - Active user account
- **Empty/No checkmark** - Inactive or disabled account

Active users can log in and access the system, while inactive users are locked out.

{{< table-actions item="user" >}}

{{< pagination >}}

## Table Features

{{< sortable-columns >}}

### Filtering
Use the search bar to filter users based on any visible field.

## Example User Entry

From the screenshot, we can see an example user:

- **Status**: ✓ Active
- **ID**: 446
- **Name**: test/Cleaner
- **Email**: test@test.com
- **Phone**: n/a
- **Department**: (empty)
- **Tags**: active
- **Last App Login**: (recent activity shown)

## Tips & Best Practices

{{% notice tip %}}
**Quick Search**: Use the search bar to quickly locate users instead of scrolling through pages. You can search by any field including ID, name, or email.
{{% /notice %}}

{{% notice info %}}
**Status Management**: Regularly review user statuses to ensure inactive employees are properly disabled to maintain system security.
{{% /notice %}}

{{% notice warning %}}
**Delete with Caution**: Deleting a user is permanent. Consider disabling users instead of deleting them to maintain historical records.
{{% /notice %}}

## Next Steps

- [Creating Users](../creating-users/) - Learn how to add new users
- [Managing Users](../managing-users/) - Edit and update user information
- [User Permissions](../permissions/) - Configure user roles and access levels
