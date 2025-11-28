---
title: "Creating Users"
weight: 2
tags: ["hr", "users", "create", "new-user", "form", "onboarding"]
categories: ["Human Resources"]
description: "Step-by-step guide to adding new users to the system"
---

# Creating New Users

Learn how to add new users to your Leviathan PCRMS system. This guide covers the complete user creation process from the "New User" form.

![Create New User Form](/images/hr/new_user.png)

## Overview

The "Create New User" feature allows administrators to add new team members to the system. The form is organized into three tabs: **GENERAL**, **GROUPS**, and **ID CARDS**.

## Accessing the New User Form

1. Navigate to **HR** → **User Dashboard**
2. Click the **"CREATE NEW USER"** button (gold button in top right)
3. The New User form will open

## User Creation Form

### General Tab

The General tab contains the essential information for creating a new user account.

#### Required Fields

| Field | Description | Required |
|-------|-------------|----------|
| **Name** | Full name of the user | ✓ Yes |
| **Email** | User's email address (used for notifications) | ✓ Yes |
| **Username** | Login username (format: `username@leviathan.systems`) | ✓ Yes |

#### Optional Fields

| Field | Description | Required |
|-------|-------------|----------|
| **Phone** | Contact phone number | No |
| **Password** | Initial password for the user account | No |
| **Expire In** | Set an expiration date for the account (if needed) | No |
| **Add Tag** | Assign tags/roles to the user (e.g., "active", "manager", "cleaner") | No |

### Username Format

The username field automatically appends `@leviathan.systems` to the username you enter. For example:
- If you enter: `testCleaner1`
- The full username becomes: `testCleaner1@leviathan.systems`

### Password Field

- The password field includes a password generator button (three dots icon) on the right
- Click the dots to generate a secure random password
- The password is masked by default for security

### Tags System

Tags help organize and categorize users by role or status:
- **Active** - User account is currently active
- **Manager** - Managerial role
- **Cleaner** - Cleaning staff role
- **Maintenance** - Maintenance staff
- Custom tags can be added as needed

To add a tag:
1. Type the tag name in the "Add Tag" field
2. Press Enter or click to add
3. Tags will appear as removable chips below the field

## Additional Tabs

### Groups Tab
Assign users to organizational groups or departments for easier management and access control.

### ID Cards Tab
Manage digital or physical ID card information for the user.

## Completing User Creation

### Save the User
1. Fill in all required fields (Name, Email, Username)
2. Optionally add Phone, Password, Tags, and Expiration date
3. Click the **"SAVE"** button (gold button at bottom right)
4. The user will be created and added to the system

### Cancel Creation
- Click the **"CANCEL"** button to discard changes and close the form
- Any unsaved information will be lost

## Step-by-Step Example

Let's create a new cleaner user:

1. **Click** "CREATE NEW USER"
2. **Enter Name**: `John Doe`
3. **Enter Email**: `john.doe@company.com`
4. **Enter Phone**: `555-1234` (optional)
5. **Create Username**: Type `johndoe` (becomes `johndoe@leviathan.systems`)
6. **Set Password**: Click the password generator or enter manually
7. **Add Tag**: Type `cleaner` and press Enter
8. **Add Tag**: Type `active` and press Enter
9. **Click** "SAVE"

## Best Practices

{{% notice tip %}}
**Strong Passwords**: Always use the password generator to create secure passwords for new users. Share passwords securely through encrypted channels.
{{% /notice %}}

{{% notice info %}}
**Username Convention**: Establish a consistent username format for your organization (e.g., first.last, firstlast, employee_id).
{{% /notice %}}

{{% notice tip %}}
**Required Tags**: Consider making certain tags mandatory for all users, such as "active" to indicate the account status.
{{% /notice %}}

{{% notice warning %}}
**Account Expiration**: Use the "Expire In" field for temporary accounts (contractors, interns) to ensure automatic deactivation.
{{% /notice %}}

## Common Use Cases

### Creating a Cleaner Account
- Name: Employee's full name
- Email: Work email
- Username: Short identifier
- Tags: `cleaner`, `active`
- Password: Auto-generate

### Creating a Manager Account
- Name: Manager's full name
- Email: Work email
- Username: Professional identifier
- Tags: `manager`, `active`, `supervisor`
- Groups: Add to management group
- Password: Auto-generate

### Creating a Temporary Account
- Name: Contractor name
- Email: Contact email
- Username: Temp identifier
- Tags: `contractor`, `active`, `temporary`
- Expire In: Set end date
- Password: Auto-generate

## After Creating a User

Once a user is created:

1. **Communicate Credentials** - Securely share the username and password with the new user
2. **Verify Access** - Ask the user to log in and confirm access
3. **Assign Permissions** - Configure additional permissions in the Groups or Settings tabs
4. **Review Dashboard** - The new user should appear in the User Dashboard

## Troubleshooting

**Username Already Exists**
- Try a different username variation
- Check if the user already exists in the system

**Email Format Error**
- Ensure email follows standard format: `name@domain.com`

**Cannot Save User**
- Verify all required fields are filled
- Check for error messages at the top of the form

## Next Steps

- [Managing Users](../managing-users/) - Edit and update existing user information
- [User Permissions](../permissions/) - Configure user roles and access levels
- [User Dashboard](../user-dashboard/) - View and search all users
