---
title: "Managing Users"
weight: 3
tags: ["hr", "users", "edit", "update", "manage", "password-reset"]
categories: ["Human Resources"]
description: "Edit and update existing user information and settings"
---

# Managing and Editing Users

Learn how to edit and update existing user information in Leviathan PCRMS. This guide covers the complete user editing process.

![Edit User Form](/images/hr/edit_user.png)

## Overview

The Edit User feature allows administrators to modify existing user accounts, update contact information, change passwords, manage tags, and adjust account settings.

## Accessing the Edit User Form

### From the User Dashboard

1. Navigate to **HR** → **User Dashboard**
2. Locate the user you want to edit
3. Click the **Edit** button (pencil icon) in the Actions column
4. The Edit User form will open

## Edit User Form

The form is organized into three tabs: **GENERAL**, **GROUPS**, and **ID CARDS**.

### General Tab

The General tab displays all the basic user information that can be edited.

![Edit User - General Tab](/images/hr/edit-user.png)

#### Editable Fields

| Field | Description | Can Edit |
|-------|-------------|----------|
| **Name** | User's full name | ✓ Yes |
| **Email** | User's email address | ✓ Yes |
| **Phone** | Contact phone number | ✓ Yes |
| **Username** | Login username (format: `username@leviathan.systems`) | ✓ Yes |
| **Password** | User's password (can be changed) | ✓ Yes |
| **Expire In** | Account expiration date | ✓ Yes |
| **Tags** | User roles and status tags | ✓ Yes |

### Example: Editing testCleaner User

From the screenshot, we can see the user "testCleaner" being edited:

- **Name**: testCleaner
- **Email**: test@test.com
- **Phone**: na
- **Username**: testCleaner1@leviathan.systems
- **Password**: (hidden for security)
- **Tags**: active

## Updating User Information

### Changing User Name
1. Click in the **Name** field
2. Update the name
3. Click **SAVE** to apply changes

### Updating Contact Information
1. **Email**: Enter new email address
2. **Phone**: Update phone number (or enter "na" if not applicable)
3. Click **SAVE**

### Changing Password
1. Click in the **Password** field
2. Option 1: Type a new password manually
3. Option 2: Click the **password generator** button (three dots icon) to create a secure password
4. The new password will be masked (shown as dots)
5. Click **SAVE**

{{% notice warning %}}
**Password Changes**: When you change a user's password, they will need to log in with the new credentials. Make sure to communicate the new password securely.
{{% /notice %}}

### Modifying Username
- The username format is fixed as `[username]@leviathan.systems`
- Edit the part before the @ symbol
- The domain remains constant

### Managing Tags

#### Adding Tags
1. Type the tag name in the **Add Tag** field
2. Press Enter or click to add
3. The tag appears as a chip below the field

#### Removing Tags
- Each tag has an **X** button
- Click the X to remove a tag
- For example, the "active" tag can be removed if the user becomes inactive

#### Common Tags
- **active** - User account is currently active
- **inactive** - User account is disabled
- **manager** - Managerial role
- **cleaner** - Cleaning staff
- **maintenance** - Maintenance staff
- **admin** - Administrator privileges

### Setting Account Expiration
1. Click the **Expire In** field
2. Select a date when the account should expire
3. Leave blank for no expiration
4. Useful for temporary workers, contractors, or interns

## Additional Tabs

### Groups Tab
- Assign or remove users from groups
- Groups help organize users by department or function
- Useful for access control and permissions

### ID Cards Tab
- Manage digital or physical ID card information
- Update card access permissions
- Track card issuance and returns

## Saving Changes

### Save Your Edits
1. Make all necessary changes in the form
2. Click the **"SAVE"** button (gold button at bottom right)
3. Changes will be applied immediately
4. The form will close and return to the User Dashboard

### Cancel Editing
- Click the **"CANCEL"** button to discard all changes
- The form will close without saving
- All modifications will be lost

## Common Editing Tasks

### Deactivating a User

When an employee leaves:
1. Open the user's edit form
2. Remove the "active" tag
3. Add an "inactive" tag
4. Optionally: Set an expiration date
5. Click **SAVE**

{{% notice tip %}}
**Don't Delete**: Instead of deleting users, deactivate them by removing the "active" tag. This preserves historical data and activity logs.
{{% /notice %}}

### Resetting a User's Password

When a user forgets their password:
1. Open the user's edit form
2. Click the password field
3. Click the password generator (three dots)
4. Copy the generated password
5. Click **SAVE**
6. Securely communicate the new password to the user

### Updating User Role

To change a user's role:
1. Open the user's edit form
2. Remove old role tag (e.g., "cleaner")
3. Add new role tag (e.g., "manager")
4. Update Groups tab if needed
5. Click **SAVE**

### Converting Temporary to Permanent User

For contractors becoming employees:
1. Open the user's edit form
2. Clear the "Expire In" date
3. Remove "contractor" or "temporary" tags
4. Add "active" and appropriate role tags
5. Update email to company email if needed
6. Click **SAVE**

## Bulk Editing

For editing multiple users:
1. Edit users one at a time using the process above
2. Use consistent tags across similar roles
3. Consider creating a standard checklist for user updates

## Best Practices

{{% notice tip %}}
**Regular Audits**: Periodically review user accounts to ensure information is up-to-date and inactive users are properly tagged.
{{% /notice %}}

{{% notice info %}}
**Tag Consistency**: Maintain a standardized list of tags across your organization for easier filtering and management.
{{% /notice %}}

{{% notice warning %}}
**Email Changes**: Changing a user's email may affect notifications and password reset functionality. Verify the new email is correct before saving.
{{% /notice %}}

## Troubleshooting

**Changes Not Saving**
- Ensure all required fields are filled
- Check for error messages
- Verify you have permission to edit users

**Username Already Exists**
- Choose a different username
- Check if another user has the same username

**Cannot Remove Tag**
- Some tags may be system-required
- Try refreshing the page and trying again

## After Editing a User

Once changes are saved:

1. **Verify Changes** - Check the User Dashboard to confirm updates
2. **Notify User** - If you changed login credentials, inform the user
3. **Test Access** - For role changes, verify the user has appropriate permissions
4. **Document Changes** - Keep a log of significant user account modifications

## Next Steps

- [User Dashboard](../user-dashboard/) - Return to view all users
- [Creating Users](../creating-users/) - Add new users to the system
- [User Permissions](../permissions/) - Configure detailed access controls
