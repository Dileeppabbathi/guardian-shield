package com.guardian.shield.data.db

import androidx.room.*
import com.guardian.shield.data.model.*
import kotlinx.coroutines.flow.Flow

@Dao
interface ThreatDao {
    @Query("SELECT * FROM threats ORDER BY detectedAt DESC")
    fun getAllThreats(): Flow<List<Threat>>
    
    @Query("SELECT * FROM threats WHERE type = :type ORDER BY detectedAt DESC")
    fun getThreatsByType(type: ThreatType): Flow<List<Threat>>
    
    @Insert
    suspend fun insert(threat: Threat): Long
    
    @Delete
    suspend fun delete(threat: Threat)
    
    @Query("DELETE FROM threats")
    suspend fun deleteAll()
}

@Dao
interface WhitelistDao {
    @Query("SELECT * FROM whitelist ORDER BY addedAt DESC")
    fun getAllWhitelist(): Flow<List<WhitelistEntry>>
    
    @Query("SELECT * FROM whitelist WHERE value = :value")
    suspend fun findByValue(value: String): WhitelistEntry?
    
    @Insert
    suspend fun insert(entry: WhitelistEntry): Long
    
    @Delete
    suspend fun delete(entry: WhitelistEntry)
}

@Dao
interface SettingsDao {
    @Query("SELECT * FROM settings WHERE id = 1")
    fun getSettings(): Flow<AppSettings>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun updateSettings(settings: AppSettings)
}

@Dao
interface StatisticsDao {
    @Query("SELECT * FROM statistics WHERE id = 1")
    fun getStatistics(): Flow<Statistics>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun updateStatistics(stats: Statistics)
}
