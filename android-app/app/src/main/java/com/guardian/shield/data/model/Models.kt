package com.guardian.shield.data.model

import androidx.room.Entity
import androidx.room.PrimaryKey
import java.util.Date

/**
 * Threat detected by the app
 */
@Entity(tableName = "threats")
data class Threat(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val url: String,
    val type: ThreatType,
    val severity: ThreatSeverity,
    val detectedAt: Date,
    val appSource: String,
    val detectionMethod: DetectionMethod,
    val mlConfidence: Float? = null,
    val userAction: UserAction = UserAction.PENDING,
    val blocked: Boolean = true
)

enum class ThreatType {
    PHISHING_URL,
    MALICIOUS_IMAGE,
    SUSPICIOUS_QR,
    MALWARE_LINK,
    SCAM_CONTENT
}

enum class ThreatSeverity {
    LOW,
    MEDIUM,
    HIGH,
    CRITICAL
}

enum class DetectionMethod {
    ML_MODEL,
    API_CHECK,
    PATTERN_MATCH,
    HYBRID
}

enum class UserAction {
    PENDING,
    BLOCKED,
    ALLOWED,
    WHITELISTED
}

/**
 * Whitelist entry for trusted sources
 */
@Entity(tableName = "whitelist")
data class WhitelistEntry(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val value: String,
    val type: WhitelistType,
    val addedAt: Date,
    val reason: String? = null
)

enum class WhitelistType {
    URL,
    DOMAIN,
    APP_PACKAGE
}

/**
 * App settings
 */
@Entity(tableName = "settings")
data class AppSettings(
    @PrimaryKey
    val id: Long = 1,
    val protectionEnabled: Boolean = true,
    val protectionLevel: ProtectionLevel = ProtectionLevel.BALANCED,
    val scanImages: Boolean = true,
    val scanUrls: Boolean = true,
    val scanQrCodes: Boolean = true,
    val autoBlock: Boolean = true,
    val notificationsEnabled: Boolean = true
)

enum class ProtectionLevel {
    PERMISSIVE,
    BALANCED,
    STRICT
}

/**
 * Statistics
 */
@Entity(tableName = "statistics")
data class Statistics(
    @PrimaryKey
    val id: Long = 1,
    val totalThreatsBlocked: Int = 0,
    val phishingUrlsBlocked: Int = 0,
    val maliciousImagesBlocked: Int = 0,
    val qrCodesBlocked: Int = 0,
    val lastScanDate: Date? = null,
    val installedDate: Date
)
