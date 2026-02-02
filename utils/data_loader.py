"""
数据加载工具类
"""
import yaml
import json
import pandas as pd
from pathlib import Path
from typing import Any, Dict, List
from loguru import logger
from openpyxl import load_workbook


class DataLoader:
    """数据加载器"""
    
    @staticmethod
    def load_yaml(file_path: str) -> Dict[str, Any]:
        """
        加载YAML文件
        
        Args:
            file_path: YAML文件路径
            
        Returns:
            字典数据
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            logger.debug(f"成功加载YAML文件: {file_path}")
            return data or {}
        except Exception as e:
            logger.error(f"加载YAML文件失败: {file_path}, 错误: {e}")
            raise
    
    @staticmethod
    def load_json(file_path: str) -> Dict[str, Any]:
        """
        加载JSON文件
        
        Args:
            file_path: JSON文件路径
            
        Returns:
            字典数据
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            logger.debug(f"成功加载JSON文件: {file_path}")
            return data
        except Exception as e:
            logger.error(f"加载JSON文件失败: {file_path}, 错误: {e}")
            raise
    
    @staticmethod
    def load_excel(file_path: str, sheet_name: str = None) -> List[Dict[str, Any]]:
        """
        加载Excel文件
        
        Args:
            file_path: Excel文件路径
            sheet_name: 工作表名称，默认为第一个工作表
            
        Returns:
            字典列表
        """
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            data = df.to_dict("records")
            logger.debug(f"成功加载Excel文件: {file_path}, 工作表: {sheet_name}")
            return data
        except Exception as e:
            logger.error(f"加载Excel文件失败: {file_path}, 错误: {e}")
            raise
    
    @staticmethod
    def get_test_data(test_name: str, data_file: str = None) -> Dict[str, Any]:
        """
        获取测试数据
        
        Args:
            test_name: 测试名称
            data_file: 数据文件路径，默认使用配置文件中的路径
            
        Returns:
            测试数据字典
        """
        from config.settings import Settings
        
        if data_file is None:
            data_file = Settings.TEST_DATA_FILE
        
        data = DataLoader.load_yaml(data_file)
        return data.get(test_name, {})

