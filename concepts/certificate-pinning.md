---
name: Certificate Pinning
type: concept
first_seen: 2022-09-04
last_updated: 2026-04-22
sources:
  - bypass-certificate-pinning.md
  - how-to-scrape-data-from-mobile-apps.md
  - jwt-tokens-and-api-scraping.md
  - http-toolkit-network-intercept.md
---

# Certificate Pinning

## Definition

Certificate pinning is a security mechanism in mobile apps that causes the app to reject any TLS certificate that does not match a specific expected certificate or public key, regardless of whether the device's OS trusts the certificate authority. It prevents man-in-the-middle inspection even on a device where the inspector's root CA has been installed.

## How It Works

Standard HTTPS validation delegates trust to the OS certificate store. If the OS trusts a CA, it trusts any certificate signed by that CA. Proxy tools like Fiddler, HTTP Toolkit, and Charles work by installing their own CA in the device's trust store, making the device trust any certificate the proxy issues.

Certificate pinning bypasses this chain. The app stores the expected server certificate's fingerprint or public key at compile time. When establishing a connection, the app compares the presented certificate against its stored expectation. If they do not match, the connection is rejected. Since the proxy's certificate does not match the hardcoded server certificate, the proxy cannot decrypt the traffic.

### Detection

The simplest way to detect pinning: install a proxy certificate on the device, configure the device to route traffic through the proxy, and try using the target app. If the app displays errors like "cannot connect," "SSL handshake failed," or returns no data while other apps work fine, the app is pinned.

### Common Pinning Implementations (Android)

- `X509TrustManager.checkServerTrusted`: Standard Java SSL validation hook. Most common target for bypass scripts.
- `X509TrustManagerImpl`: Internal implementation class.
- OkHttp's `CertificatePinner.check`: Many Android apps use OkHttp; this is its pinning hook.
- Custom network security config (Android 7+): A manifest-level config that stops user-installed CAs from being trusted by the app, even without explicit pinning code.

## Bypassing with Frida

Frida is a dynamic instrumentation toolkit that injects JavaScript into a running app process. It hooks into certificate validation functions and forces them to return success regardless of the actual certificate presented.

The standard bypass script hooks into `X509TrustManager` and related classes, replacing their validation logic with a no-op that always accepts the connection. Universal bypass scripts are available on [codeshare.frida.re](https://codeshare.frida.re).

### Setup for Android (virtual device)

```bash
# Root the AVD with RootAVD
./rootAVD.sh system-images/android-31/google_apis_playstore/arm64-v8a/ramdisk.img

# Push Frida server to the device
adb push frida-server-16.4.8-android-arm64 /data/local/tmp/frida-server
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"

# Install desktop tools
pip install frida-tools frida

# Run the bypass
frida -U -f com.target.app -l ssl_pinning_bypass.js --pause
# then: %resume
```

The bypass script must reference the MITM proxy's certificate file on the device:
```javascript
var fileInputStream = FileInputStream.$new("/data/local/tmp/FiddlerRoot.crt");
```

## HTTP Toolkit as an Alternative

HTTP Toolkit simplifies the setup for non-rooted Android devices via ADB: rooting is not needed for apps that do not use explicit certificate pinning. It installs trusted SSL certificates automatically when connecting via ADB.

For apps with pinning, HTTP Toolkit still requires a rooted device with Frida, but its integration is cleaner than the manual Frida + Fiddler setup.

## iOS Considerations

iOS apps default to trusting user-installed CA certificates (unlike Android 7+ apps). Apps that do not explicitly implement certificate pinning can be intercepted on a non-jailbroken device by installing a proxy CA certificate through Settings > General > About > Certificate Trust Settings.

For iOS apps that implement pinning, a jailbroken device with Frida or the Objection tool (a Frida-based automation framework) is required. This is more involved than the Android path.

## Known Limitations

- Not all Frida bypass scripts work with all apps. Different apps use different pinning libraries, and a script targeting `X509TrustManager` may not catch OkHttp's `CertificatePinner`.
- Third-party services within an app (Google Maps, Firebase authentication, analytics SDKs) may implement their own pinning independently of the app's main pinning logic. Bypassing the app's pinning does not automatically bypass these service-level pins.
- Some apps detect Frida's presence (via process names, specific memory regions, or timing anomalies) and refuse to start or crash when Frida is attached.
- Pinning is enforced at compile time. If the server rotates its certificate, pinned apps break until updated — this is a known operational cost of pinning that some companies accept.

## Current State (as of 2026-04)

Certificate pinning bypass via Frida on a rooted Android virtual device is the standard TWSC approach for intercepting mobile app traffic. HTTP Toolkit has simplified setup for non-pinned apps. The primary friction point is apps that use third-party services with independent pinning (notably Google services), which cannot be bypassed by the same Frida script that handles the main app.

## Related

- [mobile-app-scraping](./mobile-app-scraping.md)
- [api-scraping](./api-scraping.md)
- [tls-fingerprinting](./tls-fingerprinting.md)

## Sources

- [https://substack.thewebscraping.club/p/bypass-certificate-pinning](https://substack.thewebscraping.club/p/bypass-certificate-pinning)
- [https://substack.thewebscraping.club/p/how-to-scrape-data-from-mobile-apps](https://substack.thewebscraping.club/p/how-to-scrape-data-from-mobile-apps)
- [https://substack.thewebscraping.club/p/jwt-tokens-and-api-scraping](https://substack.thewebscraping.club/p/jwt-tokens-and-api-scraping)
- [https://substack.thewebscraping.club/p/http-toolkit-network-intercept](https://substack.thewebscraping.club/p/http-toolkit-network-intercept)
