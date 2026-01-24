package com.guardian.shield.data.db

import androidx.room.Database
import androidx.room.RoomDatabase
import androidx.room.TypeConverters
import com.guardian.shield.data.model.Threat
import com.guardian.shield.data.model.WhitelistEntry
import com.guardian.shield.data.model.AppSettings
import com.guardian.shield.data.model.Statistics

@Database(
    entities = [
        Threat::class,
        WhitelistEntry::class,
        AppSettings::class,
        Statistics::class
    ],
    version = 1,
    exportSchema = false
)
@TypeConverters(Converters::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun threatDao(): ThreatDao
    abstract fun whitelistDao(): WhitelistDao
    abstract fun settingsDao(): SettingsDao
    abstract fun statisticsDao(): StatisticsDao
}
