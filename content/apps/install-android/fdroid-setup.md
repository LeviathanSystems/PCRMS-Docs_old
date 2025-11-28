---
title: "F-Droid Setup for Automatic Updates"
weight: 1
tags: ["apps", "android", "fdroid", "installation", "automatic-updates", "repository"]
categories: ["Mobile Apps", "Installation", "Android"]
description: "Set up F-Droid to automatically receive PCRMS Office updates on your Android device"
---

# F-Droid Setup for Automatic Updates

F-Droid is an installable catalog of free and open-source applications for Android. By installing PCRMS Office through F-Droid, you'll receive automatic updates whenever a new version is released.

## What is F-Droid?

F-Droid is a trusted, open-source alternative to the Google Play Store. It offers:

- **Automatic Updates**: Apps update in the background without manual intervention
- **Privacy Focused**: No tracking or personal data collection
- **Security**: All apps are verified and built from source code
- **Transparency**: Complete visibility into what apps do

## Installation Process Overview

1. Install the F-Droid app on your Android device
2. Add the Leviathan PCRMS repository to F-Droid
3. Install PCRMS Office from the repository
4. Configure automatic updates

---

## Step 1: Install F-Droid

### Download F-Droid App

1. **Open Your Browser**
   - Launch Chrome, Firefox, or your preferred browser on your Android device

2. **Visit F-Droid Website**
   - Navigate to: [https://f-droid.org](https://f-droid.org)
   - Tap the **Download F-Droid** button
   - The `F-Droid.apk` file will download

3. **Enable Installation from Unknown Sources**
   - Open **Settings** on your device
   - Go to **Security** or **Apps & Notifications**
   - Find **Install unknown apps** or **Special app access**
   - Select your **browser** (Chrome, Firefox, etc.)
   - Enable **Allow from this source**

4. **Install F-Droid**
   - Open your **Downloads** folder
   - Tap the downloaded `F-Droid.apk` file
   - Tap **Install**
   - Tap **Open** when installation completes

---

## Step 2: Add Leviathan PCRMS Repository

F-Droid uses repositories to organize apps. You'll need to add the Leviathan repository to access PCRMS Office.

**Repository URL**: `https://fdroid.leviathan.systems/repo/`

### Add the Repository

1. **Open F-Droid App**
   - Launch the F-Droid app you just installed

2. **Access Settings**
   - Tap the **menu icon** (three horizontal lines) in the top-left corner
   - Select **Settings**

3. **Navigate to Repositories**
   - Scroll down and tap **Repositories**
   - You'll see a list of enabled repositories

4. **Add New Repository**
   - Tap the **+** icon (or **Add Repository**) in the top-right corner
   - You'll see two fields:
     - **Repository URL**: Enter `https://fdroid.leviathan.systems/repo/`
     - **Fingerprint**: Enter the fingerprint if provided (optional but recommended for security)

5. **Save the Repository**
   - Tap **Add** or **OK**
   - F-Droid will fetch the repository information

### Enable the Repository

1. **Verify Repository is Enabled**
   - In the **Repositories** list, ensure the Leviathan PCRMS repository has a checkmark
   - If not, tap the repository name and toggle it ON

2. **Update Repository**
   - Go back to the F-Droid main screen
   - Pull down to refresh or tap the **Update** icon
   - F-Droid will sync the repository and download app information

---

## Step 3: Install PCRMS Office

Now that the repository is added, you can install PCRMS Office.

### Find the App

1. **Search for PCRMS Office**
   - In the F-Droid app, tap the **search icon** (magnifying glass)
   - Type "PCRMS Office"
   - Tap on the search result

2. **View App Details**
   - You'll see the app description, version, permissions, and other details
   - Review the information to confirm it's the official PCRMS Office app

### Install the App

1. **Tap Install**
   - On the app details page, tap the **Install** button
   - F-Droid will download the APK

2. **Confirm Installation**
   - You may need to grant F-Droid permission to install apps
   - If prompted, enable **Allow from this source** for F-Droid
   - Tap **Install** in the installation prompt

3. **Wait for Installation**
   - The installation process will complete
   - You'll see a success message

4. **Open the App**
   - Tap **Open** or find PCRMS Office in your app drawer

---

## Step 4: Configure Automatic Updates

F-Droid can automatically check for and install app updates.

### Enable Automatic Updates

1. **Open F-Droid Settings**
   - Launch the F-Droid app
   - Tap the **menu icon** → **Settings**

2. **Configure Auto-Update Settings**
   - Scroll to the **Automatic Updates** section
   - Enable the following options:
     - **Automatically fetch updates**: Checks for new versions regularly
     - **Automatically install updates**: Installs updates without confirmation
     - **Only on Wi-Fi**: Recommended to save mobile data

3. **Set Update Interval** (Optional)
   - Choose how often F-Droid checks for updates
   - Recommended: Every 24 hours or twice daily

4. **Background Data**
   - Ensure F-Droid is allowed to use background data
   - Go to **Settings** → **Apps** → **F-Droid** → **Data usage**
   - Enable **Background data**

### Verify Auto-Update is Working

1. **Check for Updates Manually**
   - Open F-Droid
   - Pull down to refresh
   - Check if any updates are available for PCRMS Office

2. **View Pending Updates**
   - Tap the **menu icon** → **Updates**
   - You'll see a list of apps with available updates
   - Updates will install automatically based on your settings

---

## Managing Updates

### Manual Update Check

Even with automatic updates enabled, you can manually check:

1. Open F-Droid
2. Go to **Updates** from the menu
3. Pull down to refresh
4. Updates will appear if available

### Update Notifications

F-Droid can notify you when updates are available:

1. Go to **Settings** → **Notifications**
2. Enable **Notify when updates are available**
3. You'll receive a notification when PCRMS Office has an update

### Disable Auto-Updates for Specific Apps

If you want to control PCRMS Office updates manually:

1. Open PCRMS Office in F-Droid
2. Tap the **menu icon** (three dots)
3. Select **Settings**
4. Disable **Automatic updates** for this app only

---

## Troubleshooting

### Repository Won't Add

- **Check URL**: Verify you're using the correct repository URL
- **Internet Connection**: Ensure you have a stable internet connection
- **Clear Cache**: Go to F-Droid Settings → Clear cache
- **Fingerprint Mismatch**: If you get a fingerprint error, verify the fingerprint with your administrator

### App Not Found

- **Update Repository**: Pull down to refresh the repository list
- **Check Repository is Enabled**: Go to Settings → Repositories and verify Leviathan PCRMS is checked
- **Contact Administrator**: The app may not be published yet

### Updates Not Installing Automatically

- **Check Settings**: Verify automatic update settings are enabled
- **Battery Optimization**: Some devices restrict background processes
  - Go to **Settings** → **Battery** → **Battery optimization**
  - Find F-Droid and set to **Don't optimize**
- **Storage Space**: Ensure you have enough free space for updates
- **Background Data**: Verify F-Droid can use background data

### Installation Failed

- **Clear F-Droid Cache**: Settings → Clear cache
- **Reinstall F-Droid**: Uninstall and reinstall the F-Droid app
- **Check Permissions**: Ensure F-Droid has permission to install apps

---

## Security & Privacy

### Why F-Droid is Secure

- **Open Source**: All code is publicly auditable
- **Reproducible Builds**: Apps are built from source in a verifiable way
- **No Tracking**: F-Droid doesn't collect personal data
- **Signature Verification**: Apps are signed and verified

### Repository Fingerprint

The repository fingerprint is a security feature that ensures you're connecting to the authentic Leviathan repository. Always verify the fingerprint with your administrator when adding the repository.

### Best Practices

1. **Only Add Trusted Repositories**: Only add the official Leviathan PCRMS repository
2. **Verify Fingerprints**: Always use the fingerprint if provided
3. **Keep F-Droid Updated**: Update F-Droid itself when new versions are available
4. **Review Permissions**: Check app permissions before installation

---

## Benefits of Using F-Droid

| Feature | Benefit |
|---------|---------|
| **Automatic Updates** | Always have the latest features and security patches |
| **No Manual Downloads** | Updates happen in the background |
| **Open Source** | Transparent and trustworthy |
| **Privacy Focused** | No tracking or ads |
| **Multiple Apps** | Manage all your F-Droid apps in one place |
| **Update Notifications** | Stay informed about new versions |

---

## Support

### F-Droid Resources

- **F-Droid Documentation**: [https://f-droid.org/docs](https://f-droid.org/docs)
- **F-Droid Forum**: Community support and discussions

### PCRMS Support

If you have issues with PCRMS Office:

- **Email**: [support@leviathan.systems](mailto:support@leviathan.systems)
- **Documentation**: Visit our [Support section](/support/)
- **Android Installation**: See the [Android Installation Guide](../)

---

## Next Steps

- **Launch the App**: Open PCRMS Office and sign in with your credentials
- **Explore Features**: Check out the [Features section](/features/) to learn what you can do
- **Enable Notifications**: Configure push notifications for important updates
- **Get Help**: Visit our [Support section](/support/) for guides and FAQs

---

## Frequently Asked Questions

### Do I need to keep F-Droid open for updates?

No, F-Droid works in the background. Updates will check and install even when the app is closed.

### Will automatic updates overwrite my data?

No, updates preserve all your app data and settings. Your login information and local data remain intact.

### Can I use both F-Droid and APK installation?

We recommend choosing one method. If you install via APK first, you can switch to F-Droid by installing from the repository (it will recognize the existing installation).

### How much data do updates use?

PCRMS Office updates typically range from 20-50 MB. Use the "Only on Wi-Fi" setting to avoid using mobile data.

### Is F-Droid safe?

Yes, F-Droid is widely trusted in the open-source community. All apps are verified, and the source code is publicly available for review.
